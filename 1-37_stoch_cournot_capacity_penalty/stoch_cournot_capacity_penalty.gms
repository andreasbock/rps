*------------------------------------------------------------------*
*------ Stochastic Cournot Duopoly with Capacity Constraints ------*
*------------------------------------------------------------------*
$offlisting

set s /s0, s1/;

parameter
    a         RPS requirement
    penalty   penalty for not meeting the RPS requirement /10/
    nd_max    max generation per stage /700/
    nd_min    min generation per stage /0/
    w         wind power per scenario
    prb(s)    prob of scenario         /s0 0.5, s1 0.5/
;

variables
    p(s)        electricity price
    p_rec       price of RECs
    q_rf(s)     renewable generation in stage t
    q_rec(s)    
    q_nd(s)     non-renewable generation in stage t
    theta_pen(s) non-renewable generation covered by penalty
    theta_rec(s) non-renewable generation covered by RECs
    cost_nd(s)     cost of non-renewable generation in stage t
    gamma_rf_lo(s) dual of RF min generation constraint
    gamma_rf_hi(s) dual of RF max generation constraint
    gamma_nd_lo(s) dual of ND min generation constraint
    gamma_nd_hi(s) dual of ND max generation constraint
    psi_n(s)       dual of ND penalty-alpha constraint   
    phi_n_rec(s)   dual of non-negativity for REC-covered generation
    phi_n_pen(s)   dual of non-negativity for penalty-covered generation
    delta_n(s)
;

positive variables gamma_nd_lo, gamma_nd_hi;
positive variables gamma_rf_lo, gamma_rf_hi;
positive variables p_rec;
positive variables phi_n_pen, phi_n_rec;
positive variables delta_n;

equations
    logcst
    grd_nd_a    gradient over RF lagrangian
    grd_nd_b    gradient over RF lagrangian
    grd_nd_c    gradient over RF lagrangian
    min_gen_nd  minimum generation
    max_gen_nd  maximum generation
    penalty_cst combined penalty and alpha
    min_gen_n_pen
    min_gen_n_rec

    grd_rf_a      gradient over RF lagrangian
    grd_rf_b      gradient over RF lagrangian
    min_gen_rf  minimum generation
    max_gen_rf  maximum generation
    rec_bound

    inv_demand   inverse demand function
    mcc    market-clearing constraint
    profit_rf_c profit of the fringe
    profit_nd_c profit of the dominant firm
;

*** Inverse demand function
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_nd(s) + q_rf(s));

*** KKTs from renewable
grd_rf_a(s) .. - p(s) + 0.01*q_rf(s)  + gamma_rf_hi(s) - gamma_rf_lo(s) - delta_n(s) =e= 0;
grd_rf_b(s) .. - (1-a)*p_rec +  _n(s) =e= 0;

rec_bound(s) .. q_rf(s) - theta_pen(s) - q_rec(s)  =g= 0;

max_gen_rf(s) .. w(s) - q_rf(s) =g= 0;
min_gen_rf(s) .. q_rf(s)        =g= 0;

*** KKTs from non-renewable
grd_nd_a(s) .. - p(s) + 0.01*q_nd(s) + 20 + 0.001*q_nd(s) + gamma_nd_hi(s) - gamma_nd_lo(s) + a*psi_n(s) =e= 0;
grd_nd_b(s) .. p_rec   - psi_n(s) - phi_n_rec(s) =e= 0;
grd_nd_c(s) .. penalty - psi_n(s) - phi_n_pen(s) =e= 0;

penalty_cst(s) .. theta_pen(s) + theta_rec(s) - a*q_nd(s)  =g= 0;

max_gen_nd(s) .. nd_max - q_nd(s) =g= 0;
min_gen_nd(s) .. q_nd(s) - nd_min =g= 0;

min_gen_n_pen(s) .. theta_pen(s) =g= 0;
min_gen_n_rec(s) .. theta_rec(s) =g= 0;

*** Market-clearing of certificates
*mcc .. sum(s, prb(s)*((1-theta_rec(s))*q_rf(s) - theta_rec(s)*q_nd(s))) =g= 0;
mcc .. sum(s, prb(s)*((1-a)*q_rf(s) - a*q_nd(s))) =g= 0;

model compl
/inv_demand,
grd_rf_a,
grd_rf_b,
rec_bound.delta_n,
max_gen_rf.gamma_rf_hi,
min_gen_rf.gamma_rf_lo,
grd_nd_a,
grd_nd_b,
grd_nd_c,
penalty_cst.psi_n,
max_gen_nd.gamma_nd_hi,
min_gen_nd.gamma_nd_lo,
min_gen_n_pen.phi_n_pen,
min_gen_n_rec.phi_n_rec,
mcc.p_rec,
/;

*** Loop over all RPS levels
set exp_w /e1*e7/;

parameter q_rf_res(exp_w,s);
parameter gamma_rf_hi_res(exp_w,s);
parameter gamma_rf_lo_res(exp_w,s);
parameter q_nd_res(exp_w,s);
parameter gamma_nd_hi_res(exp_w,s);
parameter gamma_nd_lo_res(exp_w,s);
parameter p_rec_res(exp_w);
parameter p_res(exp_w,s);
parameter profits_rf_res(exp_w);
parameter profits_nd_res(exp_w);
parameter mymarg(exp_w,s);
parameter modifier_sc(s) /s0 1.2, s1 0.8/;
parameter mymcc(exp_w);
parameter theta_pen_res(exp_w,s);
parameter theta_rec_res(exp_w,s);

parameter expected_w_res(exp_w,s);

loop(exp_w,
  w(s) = (100 + 30*(ord(exp_w)))*modifier_sc(s);
  expected_w_res(exp_w,s) =w(s);

  a=0.2;
  solve compl using mcp;
  q_rf_res(exp_w,s)=q_rf.l(s);
  q_nd_res(exp_w,s)=q_nd.l(s);
  theta_rec_res(exp_w,s)=theta_rec.l(s);
  theta_pen_res(exp_w,s)=theta_pen.l(s);
  q_nd_res(exp_w,s)=q_nd.l(s);
  p_rec_res(exp_w)=p_rec.l;
  gamma_nd_hi_res(exp_w,s)=gamma_nd_hi.l(s);
  gamma_nd_lo_res(exp_w,s)=gamma_nd_lo.l(s);
  gamma_rf_hi_res(exp_w,s)=gamma_rf_hi.l(s);
  gamma_rf_lo_res(exp_w,s)=gamma_rf_lo.l(s);
  mymarg(exp_w,s)=max_gen_nd.m(s);
  mymcc(exp_w) = sum(s, prb(s)*((1-a)*q_rf.l(s) - a*q_nd.l(s)));
  p_res(exp_w,s)=p.l(s);
* profits_rf_res(i) = sum(s,prb(s)*(p.l(s) * q_rf.l(s) + (1-a)*p_rec.l*q_rf.l(s) - 90*w(s)));
* profits_nd_res(i,s) = p.l(s) * q_nd.l(s) - a*p_rec.l*q_nd.l(s) - 20*q_nd.l(s) + 0.0005*power(q_nd.l(s),2);
  profits_rf_res(exp_w) = sum(s,prb(s)*(p.l(s) * q_rf.l(s) + (1-a)*p_rec.l*q_rf.l(s) - 25*w(s)));
  profits_nd_res(exp_w) = sum(s,prb(s)*(p.l(s) * q_nd.l(s) - a*p_rec.l*q_nd.l(s) - 20*q_nd.l(s) + 0.0005*power(q_nd.l(s),2)));
);

display
p_res,
q_rf_res,
*gamma_rf_lo_res,
*gamma_rf_hi_res,
q_nd_res,
*gamma_nd_lo_res,
*gamma_nd_hi_res,
mymcc,
p_rec_res,
profits_rf_res,
profits_nd_res,
theta_rec_res,
theta_pen_res
;


$exit



************
*** Loop over all RPS levels
set i /i1*i11/;
set exp_w /e1*e50/;

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
  w(s) = 10*ord(exp_w)*modifier_sc(s);
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
*gamma_rf_lo_res,
*gamma_rf_hi_res,
q_nd_res,
*gamma_nd_lo_res,
*gamma_nd_hi_res,
p_rec_res,
p_res,
profits_rf_res,
profits_nd_res,
*expected_w_res
;
