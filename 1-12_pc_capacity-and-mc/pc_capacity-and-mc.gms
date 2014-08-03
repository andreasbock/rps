*-----------------------------------*
*------ Complementarity Model ------*
*-----------------------------------*

parameter
    a        RPS requirement
*** Curtailment cost for RF
    rf_crtl  curtailment cost of RF /15/

*** ND costs
    nd_lin_cst linear term of ND cost /20/
    nd_qdr_cst quadratic term of ND cost /0.0005/

*** Inverse demand function components
    p_cst  demand intercept /100/
    p_lin  demand modifier /0.1/

    nd_max   max generation per stage /500/
*   nd_max   max generation per stage /2000/
    nd_min   min generation per stage /0/

    rf_min   min generation per stage /0/

*** Wind "power"
    w /250/
*   w /1000/
;

scalar M constant for Fortuny-Amat linearization /4000/;

variables
    p        electricity price
    p_rec    price of RECs
    q_rf     renewable generation in stage t
    q_nd     non-renewable generation in stage t
    cost_nd  cost of non-renewable generation in stage t
    gamma_rf_lo dual of RF min generation constraint
    gamma_rf_hi dual of RF max generation constraint
    gamma_nd_lo dual of ND min generation constraint
    gamma_nd_hi dual of ND max generation constraint
*   profit_rf 
*   profit_nd
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
inv_demand .. p =e= p_cst - p_lin*(q_nd + q_rf);

*** KKTs from renewable
grd_rf .. -p+gamma_rf_hi-gamma_rf_lo - (1-a)*p_rec =e= 0;

max_gen_rf .. w - q_rf =g= 0;
min_gen_rf .. q_rf - rf_min =g= 0;

*** KKTs from non-renewable
grd_nd .. - p + gamma_nd_hi - gamma_nd_lo + 20 + 0.001*q_nd  + a*p_rec =e= 0;

max_gen_nd .. nd_max - q_nd =g= 0;
min_gen_nd .. q_nd - nd_min =g= 0;

*** Market-clearing of certificates
mcc .. (1-a)*q_rf - a*q_nd =g= 0;

model compl /inv_demand,grd_nd,grd_rf,max_gen_rf.gamma_rf_hi,min_gen_rf.gamma_rf_lo,max_gen_nd.gamma_nd_hi,min_gen_nd.gamma_nd_lo,mcc.p_rec/;

*** Loop over all RPS levels
set i /i1*i11/;

parameter q_rf_res(i);
parameter q_nd_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_rf(i);
parameter profits_nd(i);
scalar stop /0/;

loop(i,
    a=(ord(i)-1)/10;
    solve compl using mcp;
    q_rf_res(i)=q_rf.l; 
    q_nd_res(i)=q_nd.l; 
    p_rec_res(i)=p_rec.l; 
    p_res(i)=p.l; 
*   profits_rf(i) = profit_rf.l;
*   profits_nd(i) = profit_nd.l;
);

display
q_rf_res,
q_nd_res,
p_rec_res,
p_res
*profits_rf,
*profits_nd
;
