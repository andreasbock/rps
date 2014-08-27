*-- Stochastic Wind power investment --*

Sets
    s   scenarios /s0, s1/
    b   binary for expansion block discretisation /1*100/
;

Scalar
    a      RPS requirement
    n_min  minimum non-renewable production   /0/
    n_max  maximum non-renewable production   /600/
    exp_bl renewable expansion blocks         /1/
    c_inv  investment cost per unit           /5/
    c_max  investment budget                  /90000/
    d      demand for electricity             /100/
    M      constant                           /100000000/
    p_rec_param
;

Parameter
    w(s)   wind production           /s0 1.5, s1 1.0/
    p(s)   probability of scenario s /s0 0.5, s1 0.5/
;

Variables
    r_costs objective function value
    q_r(s)  renewable generation
    q_n(s)  non-renewable generation
    X_r  renewable capacity installed
    lda(s)  demand dual
    v(b)    binary
    p_rec   price of RECs
    pe(s)   power price
* Dual variables
    gam_r_lo(s)
    gam_r_hi(s)
    gam_n_lo(s)
    gam_n_hi(s)
* Used in linearization
    k(b,s)
    k_hat(b,s)
    u_n_hi(s)
    u_n_lo(s) 
    u_r_hi(s)
    u_r_lo(s)
    u_mcc
;

positive variable q_n, q_r;
positive variable p_rec;
positive variable X_r;
positive variable gam_r_lo, gam_r_hi, gam_n_lo, gam_n_hi;
positive variable lda;

binary variable v, u_n_hi, u_n_lo, u_r_hi, u_r_lo, u_mcc;

Equations
    obj       negative profits for renewable
    inv_disc  discretise the investment size
    inv_bound upper bound on investment size

    grd_lg_r  gradient over renewable lagrangian
    grd_lg_n  gradient over non-renewable lagrangian
    primal_dual primal-dual for lower-level
    demand    balance equation
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

    prim
    dual

    min_r
    min_n
*** Cournot market complementarity problem for p_rec
    grd_n      gradient over renewable lagrangian
    grd_r      gradient over non-renewable lagrangian

    inv_demand
;

* Upper-level problem
obj .. r_costs =e= c_inv*X_r
                 - exp_bl*sum(s,p(s)*w(s)*sum(b,k(b,s)))
                 - (1-a)*p_rec_param*sum(s,p(s)*q_r(s));

inv_disc .. X_r =e= exp_bl*sum(b,v(b));
inv_bound .. c_max =g= c_inv*X_r;

* KKTs for lower-level problem
grd_lg_r(s) ..                -gam_r_lo(s)+gam_r_hi(s) - lda(s) =e= 0;
grd_lg_n(s) .. 20+0.001*q_n(s)-gam_n_lo(s)+gam_n_hi(s) - lda(s) =e= 0;
demand(s)   .. d - (q_r(s) + q_n(s)) =e= 0;

n_up_a(s) .. n_max - q_n(s) =l= M*u_n_hi(s);
n_up_b(s) .. gam_n_hi(s)    =l= M*(1-u_n_hi(s));
n_up_c(s) .. n_max - q_n(s) =g= 0;

n_lo_a(s) .. q_n(s)      =l= M*u_n_lo(s);
n_lo_b(s) .. gam_n_lo(s) =l= M*(1-u_n_lo(s));

r_up_a(s) .. w(s)*X_r - q_r(s) =l= M*u_r_hi(s);
r_up_b(s) .. gam_r_hi(s)          =l= M*(1-u_r_hi(s));
r_up_c(s) .. w(s)*X_r - q_r(s) =g= 0;

r_lo_a(s) .. q_r(s)      =l= M*u_r_lo(s);
r_lo_b(s) .. gam_r_lo(s) =l= M*(1-u_r_lo(s));

*** Market-clearing of certificates
mcc_a .. sum(s, p(s)*((1-a)*q_r(s) - a*q_n(s))) =g= 0;
mcc_b .. sum(s, p(s)*((1-a)*q_r(s) - a*q_n(s))) =l= M*u_mcc;
mcc_c .. p_rec_param =l= M*(1-u_mcc);

*** Linearizing lambda term in objective
set_k(b,s)      .. k(b,s) =e= gam_r_hi(s) - k_hat(b,s);
lin_lda1_1(b,s) .. 0 =l= k(b,s);
lin_lda1_2(b,s) .. k(b,s) =l= v(b)*M;
lin_lda2_1(b,s) .. 0 =l= k_hat(b,s);
lin_lda2_2(b,s) .. k_hat(b,s) =l= (1-v(b))*M;

grd_r(s) .. -pe(s)+gam_r_hi(s)-gam_r_lo(s)-(1-a)*p_rec =e= 0;
grd_n(s) .. -pe(s)+gam_n_hi(s)-gam_n_lo(s)+20+0.001*q_n(s)+a*p_rec =e=0;

*grd_r(s) .. -pe(s)+gam_r_hi(s)-gam_r_lo(s)-(1-a)*p_rec + 0.01*q_r(s) =e= 0;
*grd_n(s) .. -pe(s)+gam_n_hi(s)-gam_n_lo(s)+20+0.001*q_n(s)+a*p_rec +0.01*q_n(s)=e=0;
inv_demand(s) .. pe(s) =e= 100 - 0.01*(q_n(s)+q_r(s));

model r_invest
/obj,
inv_disc,
inv_bound,
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
set_k
/;

min_n(s) .. q_n(s) =g= 0;
min_r(s) .. q_r(s) =g= 0;

model cournot
/inv_demand,
grd_n,
grd_r,
r_up_c.gam_r_hi,
min_r.gam_r_lo,
n_up_c.gam_n_hi,
min_n.gam_n_lo,
mcc_a.p_rec
/;

option miqcp=bonmin;
option mcp=path;

*** Diagonalisation algorithm
set it number of iterations /1*25/;
parameter prev_X_r;
parameter prev_X_n;
parameter prev_q_n(s);
parameter prev_q_r(s);
scalar error_r;
scalar error_n;
scalar done /0/;
scalar iteration;
scalar tolerance /0.1/;
parameter res_X_r(it);
parameter res_X_n(it);

* Fix initial production and REC price
p_rec_param = 0;
prev_X_r = 250;
prev_X_n = 250;

a = 1;

loop(it$(ord(it)>1 and not done),
    iteration = ord(it);
    display "*----- DIAGONALISATION ITERATION ", iteration, "-----*";

*** Solve each firm's optimisation problem using p, p_rec as parameters
    X_r.lo = 0;
    X_r.up = INF;

*** Solve for the renewable
*   Fix non-renewable production
*   q_n.fx(s) = prev_q_n(s); 
    solve r_invest min r_costs using miqcp;
* Fix initial X_r levels
    X_r.fx = X_r.l;

*** Solve Cournot problem to determine p_rec
*   q_r.fx(s) = q_r.l(s);
*   q_n.fx(s) = q_n.l(s);

*   solve cournot using mcp;
*   p_rec_param = p_rec.l;
    p_rec_param = sum(s, p(s)*(-gam_r_lo.l(s)
        +gam_r_hi.l(s)
        -(20+0.001*q_n.l(s))
        -gam_n_hi.l(s)
        +gam_n_lo.l(s)));

*** Check convergence
    error_r = abs(X_r.l - prev_X_r);
    if (error_r < tolerance,
        display "*----- ALGORITHM CONVERGED AFTER,", iteration, "-----*";
        done = 1;

    );
    prev_X_r = X_r.l;
);

display X_r.l, q_r.l, q_n.l, p_rec_param, lda.l;
*display X_n.l, X_r.l, q_r.l, q_n.l, p_rec.l, p.l;

abort$(not done) "*----- Too many iterations ! -----*"
