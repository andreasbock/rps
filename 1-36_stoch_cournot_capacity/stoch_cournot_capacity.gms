*------------------------------------------------------------------*
*------ Stochastic Cournot Duopoly with Capacity Constraints ------*
*------------------------------------------------------------------*

set s /s0, s1/;

parameter
    a         RPS requirement
    nd_max    max generation per stage /500/
    nd_min    min generation per stage /0/
    w         wind power per scenario
    prb(s)    prob of scenario         /s0 0.5, s1 0.5/
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
grd_rf(s) .. -p(s) + gamma_rf_hi(s)-gamma_rf_lo(s) - (1-a)*p_rec + 0.01*q_rf(s) =e= 0;

max_gen_rf(s) .. w(s) - q_rf(s) =g= 0;
min_gen_rf(s) .. q_rf(s) =g= 0;

*** KKTs from non-renewable
grd_nd(s) .. - p(s) + gamma_nd_hi(s) - gamma_nd_lo(s) + 45 + 0.075*q_nd(s)  + a*p_rec + 0.01*q_nd(s) =e= 0;

max_gen_nd(s) .. nd_max - q_nd(s) =g= 0;
min_gen_nd(s) .. q_nd(s) - nd_min =g= 0;

*** Market-clearing of certificates
mcc .. sum(s, prb(s)*((1-a)*q_rf(s) - a*q_nd(s))) =g= 0;

model compl
/inv_demand,
grd_nd,grd_rf,
max_gen_rf.gamma_rf_hi,
min_gen_rf.gamma_rf_lo,
max_gen_nd.gamma_nd_hi,
min_gen_nd.gamma_nd_lo,
mcc.p_rec/;

************
*** Loop over all RPS levels
set i /i1*i11/;
set exp_w /e1*e500/;

parameter q_rf_res(exp_w,i,s);
parameter gamma_rf_hi_res(exp_w,i,s);
parameter gamma_rf_lo_res(exp_w,i,s);
parameter q_nd_res(exp_w,i,s);
parameter gamma_nd_hi_res(exp_w,i,s);
parameter gamma_nd_lo_res(exp_w,i,s);
parameter p_rec_res(exp_w,i);
parameter p_res(exp_w,i,s);
parameter profits_rf_res(exp_w,i);
parameter profits_nd_res(exp_w,i);
parameter modifier_sc(s) /s0 1.2, s1 0.8/;

parameter expected_w_res(exp_w,i);

loop(exp_w,
  w(s) = ord(exp_w)*modifier_sc(s);
loop(i,
  expected_w_res(exp_w,i) = sum(s, prb(s)*(w(s)));

  a=(ord(i)-1)/10;
  solve compl using mcp;
  q_rf_res(exp_w,i,s)=q_rf.l(s);
  q_nd_res(exp_w,i,s)=q_nd.l(s);
  p_rec_res(exp_w,i)=p_rec.l;

  gamma_nd_hi_res(exp_w,i,s)=gamma_nd_hi.l(s);
  gamma_nd_lo_res(exp_w,i,s)=gamma_nd_lo.l(s);
  gamma_rf_hi_res(exp_w,i,s)=gamma_rf_hi.l(s);
  gamma_rf_lo_res(exp_w,i,s)=gamma_rf_lo.l(s);

  p_res(exp_w,i,s)=p.l(s);
* profits_rf_res(i) = sum(s,prb(s)*(p.l(s) * q_rf.l(s) + (1-a)*p_rec.l*q_rf.l(s) - 90*w(s)));
* profits_nd_res(i,s) = p.l(s) * q_nd.l(s) - a*p_rec.l*q_nd.l(s) - 20*q_nd.l(s) + 0.0005*power(q_nd.l(s),2);
  profits_rf_res(exp_w,i) = sum(s,prb(s)*(p.l(s) * q_rf.l(s) + (1-a)*p_rec.l*q_rf.l(s) - 90*w(s)));
  profits_nd_res(exp_w,i) = sum(s,prb(s)*(p.l(s) * q_nd.l(s) - a*p_rec.l*q_nd.l(s) - 20*q_nd.l(s) + 0.0005*power(q_nd.l(s),2)));
);
);

display
q_rf_res,
gamma_rf_lo_res,
gamma_rf_hi_res,
q_nd_res,
gamma_nd_lo_res,
gamma_nd_hi_res,
p_rec_res,
p_res,
profits_rf_res,
profits_nd_res,
expected_w_res
;
