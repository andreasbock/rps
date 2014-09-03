*------------------------------------------------------------------*
*------ Stochastic Cournot Duopoly with Capacity Constraints ------*
*------------------------------------------------------------------*
$offlisting

set s /s0, s1/;

parameter
    a         RPS requirement
    penalty   penalty for not meeting the RPS requirement /30/
    n_max    max generation per stage /500/
    n_min    min generation per stage /0/
    w(s)      wind power per scenario
    tau(s)    prob of scenario         /s0 4360, s1 4360/
    M /1000/
;

variables
    p(s)       electricity price
    p_rec      price of RECs
    q_r(s)     renewable generation
    q_n(s)     non-renewable generation

    mr
    mn

    cr
    cn

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

  grd_r_a
  grd_r_b
  grd_r_c

  min_r
  max_r
  min_mr
  min_cr

  mr_bound

  grd_n_a
  grd_n_b
  grd_n_c

  min_n
  max_n
  min_mn
  min_cn

  mn_bound

  mcc
;

*** Inverse demand function
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_n(s) + q_r(s));

grd_r_a(s) .. tau(s)*(- p(s) + 0.01*q_r(s)) - gamma_r_lo(s) + gamma_r_hi(s) + tau(s)*delta_r*(a-1) =e= 0;
grd_r_b .. - p_rec + delta_r - psi_r =e= 0;
grd_r_c .. penalty - phi_r - delta_r =e= 0;

min_r(s)  .. q_r(s) =g= 0;
max_r(s)  .. w(s) - q_r(s) =g= 0;
min_mr .. mr =g= 0;
min_cr .. cr =g= 0;
mr_bound .. mr - (a-1)*(sum(s, tau(s)*q_r(s))) - cr =g= 0;

grd_n_a(s) .. tau(s)*(-p(s) + 0.01*q_n(s)) + tau(s)*(20 + 0.001*q_n(s)) - gamma_n_lo(s) + gamma_n_hi(s) + tau(s)*delta_n*a =e= 0;
grd_n_b .. p_rec   - delta_n - psi_n =e= 0;
grd_n_c .. penalty - phi_n - delta_n =e= 0;

min_n(s) .. q_n(s) =g= 0;
max_n(s)  .. n_max - q_n(s) =g= 0;
min_mn .. mn =g= 0;
min_cn .. cn =g= 0;
mn_bound .. mn - a*(sum(s, tau(s)*q_n(s))) + cn =g= 0;

mcc .. cr - cn =g= 0;

model compl
/inv_demand,
grd_r_a,
grd_r_b,
grd_r_c,
min_r.gamma_r_lo,
max_r.gamma_r_hi,
min_mr.phi_r,
min_cr.psi_r,
mr_bound.delta_r,
grd_n_a,
grd_n_b,
grd_n_c,
min_n.gamma_n_lo,
max_n.gamma_n_hi,
min_mn.phi_n,
min_cn.psi_n,
mn_bound.delta_n,
mcc.p_rec
/;

*** Loop over all RPS levels
set exp_w /e1*e50/;

parameter q_r_res(exp_w,s);
parameter q_n_res(exp_w,s);
parameter p_rec_res(exp_w);
parameter p_res(exp_w,s);
parameter profit_n(exp_w);
parameter profit_r(exp_w);
parameter mn_res(exp_w);
parameter mr_res(exp_w);
parameter cn_res(exp_w);
parameter cr_res(exp_w);

parameter r_rhs(exp_w);
parameter n_rhs(exp_w);

parameter modifier_sc(s) /s0 1.2, s1 0.8/;

parameter expected_w_res(exp_w,s);

loop(exp_w,
  w(s) = 10*ord(exp_w)*modifier_sc(s);
  expected_w_res(exp_w,s) =w(s);

  a=0.3;
  solve compl using mcp;

  q_r_res(exp_w,s)=q_r.l(s);
  q_n_res(exp_w,s)=q_n.l(s);
  p_rec_res(exp_w)=p_rec.l;
  p_res(exp_w,s)=p.l(s);

  mr_res(exp_w)=mr.l;
  mn_res(exp_w)=mn.l;

  cr_res(exp_w)=cr.l;
  cn_res(exp_w)=cn.l;

  profit_r(exp_w) = sum(s, tau(s)*p.l(s)*q_r.l(s))                                          + p_rec.l*cr.l - penalty*mr.l;
  profit_n(exp_w) = sum(s, tau(s)*p.l(s)*q_n.l(s) - 20*q_n.l(s) + 0.0005*power(q_n.l(s),2)) - p_rec.l*cn.l - penalty*mn.l;

  r_rhs(exp_w) = (a-1)*(sum(s, tau(s)*q_r.l(s)));
  n_rhs(exp_w) = a*(sum(s, tau(s)*q_n.l(s)));
);

display
p_res,
q_r_res,
q_n_res,
p_rec_res,
profit_r,
profit_n,
mr_res,
mn_res,
cr_res,
cn_res,
r_rhs,
n_rhs
;
