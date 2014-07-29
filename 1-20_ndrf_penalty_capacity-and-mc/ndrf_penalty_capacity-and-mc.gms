*--- ND-RF Model with penalty and capacity constraints and new MCs

$offlisting

parameter
    a        RPS requirement
    n_max   max generation per stage /2000/
    n_min   min generation per stage /0/
    w        wind power               /2000/
    cp       compliance payment       /100/
;

variables
    n_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_n      non-renewable generation
    q_r      renewable generation
    eta_r_lo dual of lower bound on generation
    eta_r_hi dual of upper bound on generation
    u        binary for setting p_rec
    dummy    dummy for cp-p_rec
;

positive variables q_n, q_r, p, p_rec, eta_r_lo, eta_r_hi;
binary variable u;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r      gradient over RF lagrangian
    mc_a       market-clearing complementarity RHS
    mc_b       market-clearing complementarity LHS
    max_n      maximum generation of non-renewable
    min_n      minimum generation of non-renewable
    max_r      maximum generation of renewable
    min_r      minimum generation of renewable
    p_rec_disc discretise p_rec
    dummy_c
;

costs .. n_costs =e= 20*q_n+0.0005*power(q_n,2) + a*p_rec*q_n - p*q_n;
max_n .. n_max - q_n =g= 0;
min_n .. q_n - n_min =g= 0;

grd_r .. p =e= - (1-a)*p_rec + eta_r_hi - eta_r_lo;
max_r .. w - q_r =g= 0;
min_r .. q_r =g= 0;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);

mc_a .. (1-a)*q_r - a*q_n =g= 0;
mc_b .. cp - p_rec =g= 0;
p_rec_disc .. p_rec =e= cp*u;

dummy_c .. dummy =e= cp - p_rec;


model ndrf
/costs,
grd_r,
inv_demand,
max_n,
min_n,
max_r.eta_r_hi,
min_r.eta_r_lo,
mc_a.dummy,
mc_b,
*p_rec_disc,
dummy_c
/;

*** Loop over all RPS levels
set i /i1*i11/;

parameter q_r_res(i);
parameter q_n_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_r(i);
parameter profits_n(i);
parameter nd_costsp(i);

loop(i,
    a=(ord(i)-1)/10;
    solve ndrf min n_costs using mpec;
    q_r_res(i)=q_r.l; 
    q_n_res(i)=q_n.l; 
    p_rec_res(i)=p_rec.l; 
    p_res(i)=p.l; 
);

display
q_r_res,
q_n_res,
p_rec_res,
p_res
;
