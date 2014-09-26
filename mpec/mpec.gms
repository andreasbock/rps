*-- Stochastic Wind power investment MPEC --*
$offlisting

Sets
    s   scenarios /s0, s1/
    b   binary for expansion block discretisation /b1*b1000/
    nb  binary for lda discretisation /nb1*nb200/
    price_set /p1*p20/
;

Scalar
    a      RPS requirement                  /0.0/
    n_min  minimum non-renewable production /0/
    n_max  maximum non-renewable production /750/
    exp_bl renewable expansion blocks       /1/
    c_inv  investment cost per unit         /1/
    c_max  investment budget                /1000/
    d      demand for electricity           /750/
    M      constant                         /1000000000/
    penalty                                 /20/
    p_rec_p
;

Parameter
tau(s) /s0 4380, s1 4380/
rho(s) /s0 0.8, s1 0.2/
;

Variables
    r_costs objective function value
    q_r(s)  renewable generation
    q_n(s)  non-renewable generation
    X_r     renewable capacity installed
    lda(s)  demand dual
    v(nb)    binary
    p_rec   price of RECs
    mr      missing certificates
    cr      sold certificates
    mn      missing certificates
    cn      sold certificates
* Dual variables
    gam_r_lo(s)
    gam_r_hi(s)
    gam_n_lo(s)
    gam_n_hi(s)
* Used in linearization
    k(nb,s)
    k_hat(nb,s)
    u_n_hi(s)
    u_n_lo(s)
    u_r_hi(s)
    u_r_lo(s)
    u_mcc

    u_rec_mcc(b)

    u_cn(b)
    u_cr(b)

    z(b)
    z_hat(b)
;

positive variable q_r, q_n;
positive variable X_r;
positive variable gam_r_lo, gam_r_hi, gam_n_lo, gam_n_hi;
positive variable mr, mn, cr, cn;

binary variable v, u_n_hi, u_n_lo, u_r_hi, u_r_lo, u_mcc;
binary variable u_rec_mcc;

Equations
    obj       negative profits for renewable
    inv_disc  discretise the investment size
    inv_bound upper bound on investment size
    mn_bound
    mr_bound
    cert_balance_n
    cert_balance_r
    rec_bound

    grd_lg_r    gradient over renewable lagrangian
    grd_lg_n    gradient over non-renewable lagrangian
    primal_dual primal-dual for lower-level
    demand      balance equation
    n_up_a
    n_up_b
    n_up_c
    n_lo_a
    n_lo_b

    r_up_a
    r_up_b
    r_up_c
    r_lo_a
    r_lo_b
    
    mcc_a
    mcc_b
    mcc_c

    lin_lda1_1
    lin_lda1_2
    lin_lda2_1
    lin_lda2_2
    set_k
;

* Upper-level problem
obj .. r_costs =e= c_inv*X_r - sum(s,tau(s)*exp_bl*rho(s)*sum(nb,k(nb,s))) + penalty*mr - p_rec_p*cr;

inv_disc  .. X_r =e= exp_bl*sum(nb,v(nb));
inv_bound .. c_inv*X_r =l= c_max;
cert_balance_n  .. mn - a*sum(s,tau(s)*q_n(s)) + cn =g= 0;
cert_balance_r  .. mr - (a-1)*sum(s,tau(s)*q_r(s)) - cr =g= 0;
mn_bound        .. a*sum(s,tau(s)*q_n(s)) =g= mn;
mr_bound        .. a*sum(s,tau(s)*q_r(s)) =g= mr;
rec_bound       .. p_rec =l= penalty;

* KKTs for lower-level problem
grd_lg_r(s) ..                 - gam_r_lo(s) + gam_r_hi(s) - lda(s) =e= 0;
grd_lg_n(s) .. 20+0.001*q_n(s) - gam_n_lo(s) + gam_n_hi(s) - lda(s) =e= 0;
demand(s)   .. q_r(s) + q_n(s) - d =e= 0;

n_up_a(s) .. n_max - q_n(s) =l= M*u_n_hi(s);
n_up_b(s) .. gam_n_hi(s)    =l= M*(1-u_n_hi(s));
n_up_c(s) .. n_max - q_n(s) =g= 0;

n_lo_a(s) .. q_n(s)      =l= M*u_n_lo(s);
n_lo_b(s) .. gam_n_lo(s) =l= M*(1-u_n_lo(s));

r_up_a(s) .. rho(s)*X_r - q_r(s) =l= M*u_r_hi(s);
r_up_b(s) .. gam_r_hi(s)         =l= M*(1-u_r_hi(s));
r_up_c(s) .. q_r(s)              =l= rho(s)*X_r;

r_lo_a(s) .. q_r(s)      =l= M*u_r_lo(s);
r_lo_b(s) .. gam_r_lo(s) =l= M*(1-u_r_lo(s));

*** Market-clearing of certificates
mcc_a .. cr - cn =g= 0;
mcc_b .. cr - cn =l= M*u_mcc;
mcc_c .. p_rec =l= M*(1-u_mcc);

* Linearizing lambda term in objective
set_k(nb,s)    .. k(nb,s) =e= gam_r_hi(s) - k_hat(nb,s);
lin_lda1_1(nb,s) .. 0 =l= k(nb,s);
lin_lda1_2(nb,s) .. k(nb,s) =l= v(nb)*M;
lin_lda2_1(nb,s) .. 0 =l= k_hat(nb,s);
lin_lda2_2(nb,s) .. k_hat(nb,s) =l= (1-v(nb))*M;

model stoch_wind_exp
/obj,
inv_disc,
inv_bound,
rec_bound,
grd_lg_r,
grd_lg_n,
demand,
n_up_a,
n_up_b,
n_up_c,
n_lo_a,
n_lo_b,
r_up_a,
r_up_b,
r_up_c,
r_lo_a,
r_lo_b,
mcc_a,
mcc_b,
mcc_c,
lin_lda1_1,
lin_lda1_2,
lin_lda2_1,
lin_lda2_2,
set_k,
cert_balance_n,
cert_balance_r,
mn_bound,
mr_bound
/;

*
* SSB does not work
*

option miqcp = dicopt;
stoch_wind_exp.optfile = 1;

*** Loop over p_rec
scalar best /1000000000/;
scalar opt_prec;

loop(price_set,
    p_rec_p = ord(price_set);
    solve stoch_wind_exp min r_costs using miqcp;
    if (r_costs.l < best,
        best = r_costs.l;
        opt_prec = p_rec_p;
    );
);

display opt_prec;

$exit

solve stoch_wind_exp min r_costs using miqcp;

display
q_r.l,
q_n.l,
X_r.l,
lda.l,
*mr.l,
*cr.l,
gam_r_hi.l,
*gam_r_lo.l,
*gam_n_hi.l,
*gam_n_lo.l,
r_costs.l,
u_mcc.l,
cn.l,
cr.l,
p_rec.l
*k.l,
*logv.l
;
