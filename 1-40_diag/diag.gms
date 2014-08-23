*--------------------------------------*
*------ Diagonalization Approach ------*
*--------------------------------------*
$offlisting

set
    s scenario indices /s0, s1/
    b binary index for expansion block discretisation /1*100/
;

parameter
    a           RPS requirement          /0/
    w           wind power per scenario  /s0 1.2
                                          s1 1/
    c_r_inv     investment cost per renewable unit /1/
    c_r_inv_max renewable budget                   /6000/
    r_blocks    renewable investment blocks        /1/
    
    c_n_inv     investment cost per renewable unit /6/
    c_n_inv_max renewable budget                   /5000/
    n_blocks    non-renewable investment blocks    /4/
    prb(s)      probability of each scenario       /s0 0.5, s1 0.5/
;

variables
    p(s)        electricity price
    p_rec       price of RECs
    q_r(s)     renewable generation
    q_n(s)     non-renewable generation

    X_r         renewable capacity
    X_n         non-renewable capacity

    r_costs    cost of renewable generation
    n_costs    cost of non-renewable generation

    v_r(b)     binary for renewable block investment
    v_n(b)     binary for non-renewable block investment 

    gamma_r_lo(s) dual of RF min generation constraint
    gamma_r_hi(s) dual of RF max generation constraint
    gamma_n_lo(s) dual of ND min generation constraint
    gamma_n_hi(s) dual of ND max generation constraint
;

positive variables gamma_n_lo, gamma_n_hi;
positive variables gamma_r_lo, gamma_r_hi;

positive variables p_rec;
binary variables   v_r, v_n;

equations
*** Optimisation problems of the firms
    obj_r      objective of the renewable
    obj_n      objective of the non-renewable

    min_r      minimum renewable generation
    max_r      maximum renewable generation
    min_n      minimum non-renewable generation
    max_n      maximum non-renewable generation

    inv_r_disc discretise renewable investment
    r_budget   renewable investment budget constraint

    inv_n_disc discretise non-renewable investment
    n_budget   non-renewable investment budget constraint

*** Cournot market complementarity problem
    grd_n      gradient over renewable lagrangian
    grd_r      gradient over non-renewable lagrangian
 
*** Miscellaneous constraints
    inv_demand inverse demand function
    mcc        market-clearing constraint

    profit_rf_c profit of the fringe
    profit_nd_c profit of the dominant firm
;

*** Optimisation problem of the renewable
obj_r      .. r_costs =e= c_r_inv*X_r - sum(s, prb(s)*(p(s)*q_r(s) + (1-a)*p_rec*q_r(s)));
min_r(s)   .. q_r(s) =g= 0;
max_r(s)   .. w(s)*X_r =g= q_r(s); 
inv_r_disc .. X_r =e= r_blocks * sum(b,v_r(b));
r_budget   .. c_r_inv_max =g= c_r_inv*X_r;

model r_invest
/obj_r,
min_r,
max_r,
inv_r_disc,
r_budget/;

*** Optimisation problem of the non-renewable
obj_n      .. n_costs =e= c_n_inv*X_n - sum(s, prb(s)*(p(s)*q_n(s) - a*p_rec*q_n(s)));
min_n(s)   .. q_n(s) =g= 0;
max_n(s)   .. X_n =g= q_n(s);
inv_n_disc .. X_n =e= n_blocks * sum(b,v_n(b));
n_budget   .. c_n_inv_max =g= c_n_inv*X_n;

model n_invest
/obj_n,
min_n,
max_n,
inv_n_disc,
n_budget/;

*** Market optimisation problem
grd_r(s) .. -p(s)+gamma_r_hi(s)-gamma_r_lo(s)-(1-a)*p_rec-0.01*q_r(s) =e= 0;
grd_n(s) .. -p(s)+gamma_n_hi(s)-gamma_n_lo(s)-20+0.001*q_n(s)+a*p_rec-0.01*q_n(s)=e=0;

mcc .. sum(s, prb(s)*((1-a)*q_r(s) - a*q_n(s))) =g= 0;
inv_demand(s) .. p(s) =e= 100 - 0.01*(q_n(s) + q_r(s));

model cournot
/inv_demand,
grd_n,
grd_r,
max_r.gamma_r_hi,
min_r.gamma_r_lo,
max_n.gamma_n_hi,
min_n.gamma_n_lo,
mcc.p_rec/;

option minlp=bonmin;

************
*p.fx(s)=100;
*p_rec.fx = 100;
*solve r_invest min r_costs using minlp;
*q_r.fx(s) = q_r.l(s);
*$exit
************

*** Diagonalisation algorithm
set it number of iterations /1*10/;
parameter X_r_res(it);
parameter X_n_res(it);
scalar error_r;
scalar error_n;
scalar done /0/;
scalar iteration;
scalar tolerance /0.1/;

* Fix initial X_{r,n}
*X_r.fx = 100;
*X_n.fx = 100;
X_r_res('1') = 200;
X_n_res('1') = 300;
p.fx(s) = 40;
p_rec.fx = 0;

loop(it$(ord(it)>1 and not done),
    iteration = ord(it);
    display "*----- DIAGONALISATION ITERATION ", iteration, "-----*";

*** Solve each firm's optimisation problem using p, p_rec as parameters
*   Free variables X_{r,n}
    X_r.lo = 0;
    X_r.up = INF;
    X_n.lo = 0;
    X_n.up = INF;
    solve r_invest min r_costs using minlp;
    solve n_invest min n_costs using minlp;
* Fix initial X_{r,n} levels
    X_r.fx = X_r.l;
    X_n.fx = X_n.l;

*** Solve Cournot problem to determine p, p_rec
*   Free variables p, p_rec
    p.lo(s)  = (-INF);
    p.up(s)  = INF;
    p_rec.lo = 0;
    p_rec.up = INF;
    solve cournot using mcp;
*   Fix p, p_rec
    p.fx(s)  = p.l(s);
    p_rec.fx = p_rec.l;

*** Check convergence
    error_r = abs(X_r_res(it) - X_r_res(it-1));
    error_n = abs(X_n_res(it) - X_n_res(it-1));
    if (error_r < tolerance and error_n < tolerance,
        display "*----- ALGORITHM CONVERGED AFTER,", iteration, "-----*";
        done = 1;

        display X_n.l, X_r.l, q_r.l, q_n.l, p_rec.l, p.l;
    );
);

abort$(not done) "*----- Too many iterations ! -----*"








