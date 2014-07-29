*--- ND-RF Model with new MC and capacity constraints

$offlisting

parameter
    a        RPS requirement
    n_max   max generation per stage /2000/
    n_min   min generation per stage /0/
    w        wind power               /2000/
;

variables
    n_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_n      non-renewable generation
    q_r      renewable generation
    eta_r_lo dual of lower bound on generation
    eta_r_hi dual of upper bound on generation
;

positive variables q_n, q_r, p, p_rec, eta_r_lo, eta_r_hi;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r      gradient over RF lagrangian
    mc         market-clearing complementarity
    max_n      maximum generation of non-renewable
    min_n      minimum generation of non-renewable
    max_r      maximum generation of renewable
    min_r      minimum generation of renewable
;

costs .. n_costs =e= 20*q_n+0.0005*power(q_n,2) + a*p_rec*q_n - p*q_n;
max_n .. n_max - q_n =g= 0;
min_n .. q_n - n_min =g= 0;

grd_r .. p =e= - (1-a)*p_rec + eta_r_hi - eta_r_lo;
max_r .. w - q_r =g= 0;
min_r .. q_r =g= 0;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);
mc .. (1-a)*q_r - a*q_n =g= 0;

model ndrf
/costs,
grd_r,
inv_demand,
max_n,
min_n,
max_r.eta_r_hi,
min_r.eta_r_lo,
mc.p_rec/;

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
