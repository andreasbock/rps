*-----------------------------*
*------ Stochastic NDRF ------*
*-----------------------------*

$offlisting

set s /s0, s1/;

parameter
    a        RPS requirement
    n_max    max generation per stage /5000/
    n_min    min generation per stage /0/
    w(s)     wind power per scenario
    tau(s)   prob of scenario         /s0 4360, s1 4360/
    M        for linearisation        /1000000000/
    rho(s)   capacity factors         /s0 1, s1 0.6/;
;

variables
    costsv         objective function variable
    p(s)           electricity price
    p_rec          price of RECs
    q_r(s)         renewable generation
    q_n(s)         non-renewable generation

    gamma_r_lo(s)  dual of lower bound generation for the renewable
    gamma_r_hi(s)  dual of lower bound generation for the renewable
;

positive variables gamma_r_lo, gamma_r_hi;
positive variables p_rec;

equations
    costs      objective function
    inv_demand inverse demand function

    grd_r      gradient over lagrangian of the renewable

    max_n      maximum generation of non-renewable
    min_n      minimum generation of non-renewable
    max_r      maximum generation of renewable
    min_r      minimum generation of renewable

    mcc    market-clearing complementarity
;

*** Inverse demand function
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_n(s) + q_r(s));

costs .. costsv =e= sum(s,tau(s)*(20*q_n(s)+0.0005*power(q_n(s),2))) - sum(s,tau(s)*p(s)*q_n(s)) + a*p_rec*sum(s,tau(s)*q_n(s));

grd_r(s) .. - tau(s)*p(s) - gamma_r_lo(s) + gamma_r_hi(s) - (1-a)*tau(s)*p_rec =e= 0;
min_r(s)  .. q_r(s) =g= 0;
max_r(s)  .. rho(s)*w(s) - q_r(s) =g= 0;

min_n(s) .. q_n(s) =g= 0;
max_n(s)  .. n_max - q_n(s) =g= 0;

mcc .. sum(s, tau(s)*(1-a)*q_r(s)) - sum(s,tau(s)*a*q_n(s)) =g= 0;

model ndrf_stoch
/inv_demand,
grd_r,
min_r.gamma_r_lo,
max_r.gamma_r_hi,
costs,
min_n,
max_n,
mcc.p_rec
/;

a=0.5;

*** Loop over all different capacity levels for the renewable
set exp_w /e1*e80/;
scalar step /10/;

parameter p_rec_res(exp_w);
parameter profit_n(exp_w);
parameter profit_r(exp_w);

loop(exp_w,
  w(s)=step*ord(exp_w);
  
  solve ndrf_stoch min costsv using mpec;

  p_rec_res(exp_w)=p_rec.l;
  profit_r(exp_w) = sum(s, tau(s)*p.l(s)*q_r.l(s))                                      + (1-a)*p_rec.l*sum(s,tau(s)*q_r.l(s));
  profit_n(exp_w) = sum(s, tau(s)*p.l(s)*q_n.l(s) - 20*q_n.l(s) + 0.0005*power(q_n.l(s),2)) - a*p_rec.l*sum(s,tau(s)*q_r.l(s));
);

display
p_rec_res,
profit_r,
profit_n
;
