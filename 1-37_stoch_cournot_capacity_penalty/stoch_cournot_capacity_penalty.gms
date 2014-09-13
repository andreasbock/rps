*------------------------------------------------------------------*
*------ Stochastic Cournot Duopoly with Capacity Constraints ------*
*------------------------------------------------------------------*
$offlisting

set s /s0, s1/;
set alpha /a0,a2,a5/;

parameter
    a         RPS requirement                             /0.0/
    penalty   penalty for not meeting the RPS requirement /10/
    r_invest  investment cost for the renewable           /200000/
    n_max     max generation per stage                    /1000/
    n_min     min generation per stage                    /0/
    w         installed wind capacity
    tau(s)    prob of scenario                            /s0 4380, s1 4380/
    n_cst                                                 /20/
    n_lin                                                 /0.04/
    opt_w
    rho(s) /s0 0.8, s1 0.2/;
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
inv_demand(s) .. p(s) =e= 100 - 0.1*(q_n(s) + q_r(s));

*grd_r_a(s) .. -tau(s)*p(s) + tau(s)*0.1*q_r(s) - gamma_r_lo(s) + gamma_r_hi(s) + tau(s)*delta_r*(a-1) =e= 0;
grd_r_a(s) .. -tau(s)*p(s)                     - gamma_r_lo(s) + gamma_r_hi(s) + tau(s)*delta_r*(a-1) =e= 0;
grd_r_b .. - p_rec + delta_r - psi_r =e= 0;
grd_r_c .. penalty - phi_r - delta_r =e= 0;

min_r(s)  .. q_r(s) =g= 0;
max_r(s)  .. rho(s)*w - q_r(s) =g= 0;
min_mr .. mr =g= 0;
min_cr .. cr =g= 0;
mr_bound .. mr - (a-1)*(sum(s, tau(s)*q_r(s))) - cr =g= 0;

*grd_n_a(s) .. -tau(s)*p(s) + tau(s)*0.1*q_n(s) + tau(s)*(n_cst + n_lin*q_n(s)) - gamma_n_lo(s) + gamma_n_hi(s) + tau(s)*delta_n*a =e= 0;
grd_n_a(s) .. -tau(s)*p(s)                     + tau(s)*(n_cst + n_lin*q_n(s)) - gamma_n_lo(s) + gamma_n_hi(s) + tau(s)*delta_n*a =e= 0;
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
set exp_w /e1*e80/;
parameter p_rec_res(exp_w);
parameter w_res(exp_w);
parameter profit_n(exp_w);
parameter profit_r(exp_w);
scalar    step /10/;

loop(exp_w,
  w = step*ord(exp_w);

  solve compl using mcp;

  p_rec_res(exp_w)=p_rec.l;
  w_res(exp_w) = w;
  profit_r(exp_w) = sum(s, tau(s)*p.l(s)*q_r.l(s))                          + p_rec.l*cr.l - penalty*mr.l - r_invest*step*ord(exp_w);
  profit_n(exp_w) = sum(s, tau(s)*p.l(s)*q_n.l(s) - n_cst*q_n.l(s) + (n_lin/2)*power(q_n.l(s),2)) - p_rec.l*cn.l - penalty*mn.l;
);

display p_rec_res, profit_r, profit_n;

*$exit

scalar optimal_w /-1000000000000000000000000/;

  loop(exp_w,
    if(optimal_w < profit_r(exp_w),
      optimal_w = profit_r(exp_w);
      opt_w = w_res(exp_w);
    );
  );

display opt_w;
*display
*p_res,
*q_r_res,
*q_n_res,
*p_rec_res,
*profit_n,
*profit_r
*mr_res,
*mn_res,
*cr_res,
*cn_res,
*r_rhs,
*n_rhs,
*expected_w_res
*;