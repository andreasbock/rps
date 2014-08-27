*------------------------------------------------------------------*
*------ Stochastic Cournot Duopoly with Capacity Constraints ------*
*------------------------------------------------------------------*

set s /s0, s1/;

parameter
    a         RPS requirement
    nd_max    max generation per stage /500/
    nd_min    min generation per stage /0/
    w         wind power per scenario  /s0 200
                                        s1 300/
;

variables
    p(s)        electricity price
    p_rec       price of RECs
    q_rf(s)     renewable generation in stage t
    q_nd(s)     non-renewable generation in stage t
    cost_nd(s)  cost of non-renewable generation in stage t
    gamma_rf_lo(s) dual of RF min generation constraint
    gamma_rf_hi(s) dual of RF max generation constraint
    gamma_nd_lo(s) dual of ND min generation constraint
    gamma_nd_hi(s) dual of ND max generation constraint
;

positive variables gamma_nd_lo, gamma_nd_hi;
positive variables gamma_rf_lo, gamma_rf_hi;
positive variables p_rec;

equations
    grd_nd     gradient over RF lagrangian
    min_gen_nd minimum generation
    max_gen_nd maximum generation

    grd_rf       gradient over RF lagrangian
    min_gen_rf minimum generation
    max_gen_rf maximum generation

    inv_demand   inverse demand function
    mcc    market-clearing constraint
    profit_rf_c profit of the fringe
    profit_nd_c profit of the dominant firm
;

*** Inverse demand function
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_nd(s) + q_rf(s));

*** KKTs from renewable
grd_rf(s) .. -p(s) + gamma_rf_hi(s)-gamma_rf_lo(s) - (1-a)*p_rec - 0.01*q_rf(s) =e= 0;

max_gen_rf(s) .. w(s) - q_rf(s) =g= 0;
min_gen_rf(s) .. q_rf(s) =g= 0;

*** KKTs from non-renewable
grd_nd(s) .. - p(s) + gamma_nd_hi(s) - gamma_nd_lo(s) + 20 + 0.001*q_nd(s)  + a*p_rec - 0.01*q_nd(s) =e= 0;

max_gen_nd(s) .. nd_max - q_nd(s) =g= 0;
min_gen_nd(s) .. q_nd(s) - nd_min =g= 0;

*** Market-clearing of certificates
mcc .. sum(s, p(s)*((1-a)*q_rf(s) - a*q_nd(s))) =g= 0;

model compl /inv_demand,grd_nd,grd_rf,max_gen_rf.gamma_rf_hi,min_gen_rf.gamma_rf_lo,max_gen_nd.gamma_nd_hi,min_gen_nd.gamma_nd_lo,mcc.p_rec/;

*** Loop over all RPS levels
set i /i1*i11/;
set exp_w /e1*e50/;
parameter q_r_res(i);
parameter q_n_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_r_res(exp_w,i);
parameter profits_n_res(exp_w,i);
scalar stop /0/;

*loop(exp_w,
*    w = 10*ord(exp_w);
loop(i,
    a=(ord(i)-1)/10;
    solve compl using mcp;
    
    q_r_res(i)=q_r.l; 
    q_n_res(i)=q_n.l; 
    p_rec_res(i)=p_rec.l; 
    p_res(i)=p.l; 
*    profits_r_res(exp_w,i) = p.l * q_r.l + (1-a)*p_rec.l*q_r.l - 5*w;
*    profits_rf_res(exp_w,i) = p.l * q_rf.l + (1-a)*p_rec.l*q_rf.l - 5*q_rf.l;
*    profits_n_res(exp_w,i) = p.l * q_n.l - a*p_rec.l*q_n.l - 20*q_n.l + 0.0005*power(q_n.l,2);
*    profits_rf_res(i) = profit_rf.l;
*    profits_nd_res(i) = profit_nd.l;
);
);

display
q_rf_res,
q_nd_res,
p_rec_res, 
p_res
*profits_r_res,
*profits_n_res
*w
;
