*--- ND-RF Model with new MC and capacity constraints and penalty term
$offlisting

set s /s0, s1/;

parameter
    a         RPS requirement
    penalty   penalty for not meeting the RPS requirement /20/
    n_max    max generation per stage /4000/
    n_min    min generation per stage /0/
    w(s)      wind power per scenario /s0 2000, s1 2500/
    tau(s)    prob of scenario         /s0 4360, s1 4360/
;

variables
    n_costs profit of the non-renewable dominant

    p(s)       electricity price
    p_rec      price of RECs
    q_r(s)     renewable generation
    q_n(s)     non-renewable generation

    mr
    mn

    cr
    cn

    gamma_r_lo(s)
    gamma_r_hi(s)

    phi_r
    delta_r
    psi_r
;

positive variables gamma_n_lo, gamma_n_hi;
positive variables gamma_r_lo, gamma_r_hi;
positive variables p_rec;
positive variables phi_n, phi_r;
positive variables psi_n, psi_r;
positive variables delta_n, delta_r;

equations
    costs
    max_n
    min_n
    min_mn
    min_cn
    mn_bound

    grd_r_a
    grd_r_b
    grd_r_c
    min_r
    max_r
    min_mr
    min_cr
    mr_bound

    mcc
    inv_demand
;

costs .. n_costs =e= sum(s,tau(s)*(20*q_n(s) +0.0005*power(q_n(s),2) -p(s)*q_n(s))) + p_rec*cn + penalty*mn;

min_n(s) .. q_n(s) =g= 0;
max_n(s) .. n_max - q_n(s) =g= 0;
min_mn .. mn =g= 0;
min_cn .. cn =g= 0;

mn_bound .. mn - a*(sum(s, tau(s)*q_n(s))) + cn =g= 0;

mcc .. cr - cn =g= 0;
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_n(s)+q_r(s));

grd_r_a(s) .. - tau(s)*p(s) - gamma_r_lo(s) + gamma_r_hi(s) + tau(s)*delta_r*(a-1) =e= 0;
grd_r_b .. - p_rec + delta_r - psi_r =e= 0;
grd_r_c .. penalty - phi_r - delta_r =e= 0;

min_r(s) .. q_r(s) =g= 0;
max_r(s) .. w(s) - q_r(s) =g= 0;
min_mr .. mr =g= 0;
min_cr .. cr =g= 0;
mr_bound .. mr - (a-1)*(sum(s, tau(s)*q_r(s))) - cr =g= 0;


model ndrf_penalty
/costs,
max_n,
min_n,
min_mn,
min_cn,
mn_bound,
grd_r_a,
grd_r_b,
grd_r_c,
min_r.gamma_r_lo,
max_r.gamma_r_hi,
min_mr.phi_r,
min_cr.psi_r,
mr_bound.delta_r,
mcc.p_rec,
inv_demand
/;

a = 0.4;
solve ndrf_penalty using qcp min n_costs;
display q_n.l, q_r.l, p_rec.l;

$exit

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

parameter expected_w_res(exp_w);

loop(exp_w,
  w(s) = 50*ord(exp_w)*modifier_sc(s);
  expected_w_res(exp_w)=sum(s, w(s));

  a=0.9;
  solve ndrf_penalty using qcp min n_costs;

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
expected_w_res,
p_res,
q_r_res,
q_n_res,
p_rec_res,
profit_r,
profit_n,
mr_res,
mn_res,
cr_res,
cn_res
*r_rhs,
*n_rhs
;
