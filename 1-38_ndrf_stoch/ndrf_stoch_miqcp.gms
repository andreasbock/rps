*-----------------------------*
*------ Stochastic NDRF ------*
*-----------------------------*
$offlisting

set s /s0, s1/;

parameter
    a        RPS requirement          /0.0/
    n_max    max generation per stage /1000/
    n_min    min generation per stage /0/
    w(s)     wind power per scenario
    tau(s)   hours in segment s       /s0 4360, s1 4360/
    rho(s)   capacity factors         /s0 1, s1 0.6/
    M        used in linearisation    /1000000000/
;

variables
    costsv     objective
    p(s)       electricity price
    p_rec      price of RECs
    q_r(s)     renewable generation
    q_n(s)     non-renewable generation

    gamma_r_lo(s) dual of renewable lower generation bound
    gamma_r_hi(s) dual of renewable upper generation bound

* Binaries for linearisation
    u_mc
    u_max(s)
    u_min(s)
;

positive variables gamma_r_lo, gamma_r_hi;
positive variables p_rec;
binary   variables u_mc,u_max,u_min;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r      gradient over RF lagrangian

    max_n      maximum generation of non-renewable
    min_n      minimum generation of non-renewable
    max_r      maximum generation of renewable
    min_r      minimum generation of renewable
    mc_a    market-clearing complementarity
    mc_b    market-clearing complementarity
    mc_c    market-clearing complementarity

* Complementary slackness:
    min_mc_a
    min_mc_b
    max_mc_a
    max_mc_b
;

*** Inverse demand function
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_n(s) + q_r(s));

costs .. costsv =e= sum(s,tau(s)*(20*q_n(s)+0.0005*power(q_n(s),2)))
                  - sum(s,tau(s)*p(s)*q_n(s)) + a*p_rec*sum(s,tau(s)*q_n(s));

grd_r(s) .. - tau(s)*p(s) - gamma_r_lo(s) + gamma_r_hi(s) - (1-a)*tau(s)*p_rec =e= 0;

min_r(s)  .. q_r(s) =g= 0;
max_r(s)  .. w(s) - q_r(s) =g= 0;

min_n(s) .. q_n(s) =g= 0;

min_mc_a(s) .. q_n(s) =l= M*u_min(s);
min_mc_b(s) .. gamma_r_lo(s) =l= M*(1-u_min(s));

max_n(s)  .. n_max - q_n(s) =g= 0;

max_mc_a(s) .. w(s) - q_r(s) =l= M*u_max(s);
max_mc_b(s) .. gamma_r_hi(s) =l= M*(1-u_max(s));

mc_a .. sum(s, tau(s)*(1-a)*q_r(s)) - sum(s,tau(s)*a*q_n(s)) =l= M*u_mc;
mc_b .. p_rec               =l= M*(1-u_mc);
mc_c .. sum(s, tau(s)*(1-a)*q_r(s)) - sum(s,tau(s)*a*q_n(s)) =g= 0;

model ndrf_stoch
/inv_demand,
grd_r,
min_r,
max_r,
min_mc_a,
min_mc_b,
max_mc_a,
max_mc_b,
costs,
min_n,
max_n,
mc_a,
mc_b,
mc_c
/;

*** Loop over all RPS levels
set exp_w /e1*e80/;

parameter p_rec_res(exp_w);
parameter profit_n(exp_w);
parameter profit_r(exp_w);
scalar    step    /10/;

loop(exp_w,
  w(s)=step*ord(exp_w)*rho(s);

  solve ndrf_stoch min costsv using miqcp;

  p_rec_res(exp_w)=p_rec.l;

  profit_r(exp_w) = sum(s, tau(s)*p.l(s)*q_r.l(s))
                     + (1-a)*p_rec.l*sum(s,tau(s)*q_r.l(s));
  profit_n(exp_w) = sum(s, tau(s)*p.l(s)*q_n.l(s) - 20*q_n.l(s)
                     + 0.0005*power(q_n.l(s),2))
                     - a*p_rec.l*sum(s,tau(s)*q_r.l(s));
);

display
p_rec_res,
profit_r,
profit_n
;
