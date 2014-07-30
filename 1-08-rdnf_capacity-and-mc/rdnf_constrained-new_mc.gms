*-------------------------*
*------ RD-NF Model ------*
*-------------------------*

parameter
    a        RPS requirement
*** Curtailment cost for RF
    rf_crtl  curtailment cost of RF /15/

*** ND costs
    nd_lin_cst linear term of ND cost /20/
    nd_qdr_cst quadratic term of ND cost /0.0005/

*** Inverse demand function components
    p_cst  demand intercept /100/
    p_lin  demand modifier /0.001/

    nd_max   max generation per stage /2000/
*   Redundant constraint, but is included if we want to up it
    nd_min   min generation per stage /0/

*** Wind "power"
    w /2000/
;

variables
    r_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_n      non-renewable generation in stage t
    q_r      renewable generation in stage t
    u_mc     linearization of REC market-clearing
    eta_nd_lo
    eta_nd_hi
    eta_rf_lo
    eta_rf_hi
;

positive variables q_nd, q_rf, p, p_rec;
positive variables eta_nd_lo, eta_nd_hi, eta_rf_lo, eta_rf_hi;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_nd     gradient over RF lagrangian
    mc         market-clearing complementarity
    max_nd     maximum generation of non-renewable dominant
    min_nd     minimum generation of non-renewable dominant
    max_rf     maximum generation of renewable fringe
    min_rf     minimum generation of renewable fringe
;

** ND cost fnc
costs .. r_costs =e= a*p_rec*q_r - p*q_r;
max_nd .. nd_max - q_n =g= 0;
min_nd .. q_n - nd_min =g= 0;

*** KKTs from renewable fringe
grd_nd .. p =e= - (1-a)*p_rec + eta_nd_hi - eta_nd_lo;
max_rf .. w - q_r =g= 0;
min_rf .. q_r =g= 0;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);

mc .. (1-a)*q_r - a*q_n =g= 0;

model ndrf /costs,
grd_nd,
inv_demand,
max_nd.eta_nd_hi,
min_nd.eta_nd_lo,
max_rf,
min_rf,
mc.p_rec
/;

*** Loop over all RPS levels
set i /i1*i11/;

parameter q_rf_res(i);
parameter q_nd_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_rf(i);
parameter profits_nd(i);

loop(i,
    a=(ord(i)-1)/10;
    solve ndrf min r_costs using mpec;
    q_rf_res(i)=q_r.l; 
    q_nd_res(i)=q_n.l; 
    p_rec_res(i)=p_rec.l; 
    p_res(i)=p.l; 
);

display
q_rf_res,
q_nd_res,
p_rec_res,
p_res
*nd_costsp
;

$exit
