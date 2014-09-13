*------------------------------------------------------------------*
*------ Stochastic Cournot Duopoly with Capacity Constraints ------*
*------------------------------------------------------------------*
$offlisting

set s /s0, s1/;

parameter
    a         RPS requirement
    n_max    max generation per stage /500/
    n_min    min generation per stage /0/
    w(s)      wind power per scenario
    tau(s)    prob of scenario         /s0 4360, s1 4360/
;

variables
    p(s)       electricity price
    p_rec      price of RECs
    q_r(s)     renewable generation
    q_n(s)     non-renewable generation

    gamma_n_lo(s)
    gamma_n_hi(s)
    gamma_r_lo(s)
    gamma_r_hi(s)

    phi_n
    phi_r

    delta_n
    delta_r

    psi_n
    psi_r
;

positive variables gamma_n_lo, gamma_n_hi;
positive variables gamma_r_lo, gamma_r_hi;
positive variables p_rec;
positive variables phi_n, phi_r;
positive variables psi_n, psi_r;
positive variables delta_n, delta_r;

equations
  inv_demand

  grd_r
  min_r
  max_r

  grd_n
  min_n
  max_n

  mcc
;

*** Inverse demand function
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_n(s) + q_r(s));

grd_r(s) .. tau(s)*(-p(s) + 0.01*q_r(s)) - gamma_r_lo(s) + gamma_r_hi(s) - (1-a)*tau(s)*p_rec =e= 0;

min_r(s)  .. q_r(s) =g= 0;
max_r(s)  .. w(s) - q_r(s) =g= 0;

grd_n(s) .. tau(s)*(-p(s) + 0.01*q_n(s)) + tau(s)*(20 + 0.001*q_n(s)) - gamma_n_lo(s) + gamma_n_hi(s) + a*tau(s)*p_rec =e= 0;

min_n(s) .. q_n(s) =g= 0;
max_n(s) .. n_max - q_n(s) =g= 0;

mcc .. sum(s, tau(s)*(1-a)*q_r(s)) - sum(s,tau(s)*a*q_n(s)) =g= 0;
*mcc .. sum(s, tau(s)*((1-a)*q_r(s) - a*q_n(s))) =g= 0;

model compl
/inv_demand,
grd_r,
min_r.gamma_r_lo,
max_r.gamma_r_hi,
grd_n,
min_n.gamma_n_lo,
max_n.gamma_n_hi,
mcc.p_rec
/;

*** Loop over all RPS levels
set exp_w /e1*e80/;

parameter q_r_res(exp_w,s);
parameter q_n_res(exp_w,s);
parameter p_rec_res(exp_w);
parameter p_res(exp_w,s);
parameter profit_n(exp_w);
parameter profit_r(exp_w);
scalar eta;

parameter modifier_sc(s) /s0 1, s1 0.6/;

parameter expected_w_res(exp_w,s);

loop(exp_w,
  w(s) = 10*ord(exp_w)*modifier_sc(s);
  expected_w_res(exp_w,s) =w(s);

  a=0.0;
  solve compl using mcp;

  q_r_res(exp_w,s)=q_r.l(s);
  q_n_res(exp_w,s)=q_n.l(s);
  p_rec_res(exp_w)=p_rec.l;
  p_res(exp_w,s)=p.l(s);

  profit_r(exp_w) = sum(s, tau(s)*p.l(s)*q_r.l(s))                                      + (1-a)*p_rec.l*sum(s,tau(s)*q_r.l(s));
  profit_n(exp_w) = sum(s, tau(s)*p.l(s)*q_n.l(s) - 20*q_n.l(s) + 0.0005*power(q_n.l(s),2)) - a*p_rec.l*sum(s,tau(s)*q_r.l(s));

  eta = sum(s,q_r.l(s)) / sum(s,q_n.l(s)+q_r.l(s));
);

display
p_res,
q_r_res,
q_n_res,
p_rec_res,
profit_r,
eta,
profit_n
;
