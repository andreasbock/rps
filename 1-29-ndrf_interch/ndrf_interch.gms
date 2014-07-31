*--- ND-RF Model

$offlisting

parameter
    a        RPS requirement
    nd_max   max generation per stage /2000/
    nd_min   min generation per stage /0/
    w        wind power               /2000/
;

variables
    nd_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_n      non-renewable generation
    q_r      renewable generation
;

positive variables q_n, q_r, p, p_rec;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r      gradient over RF lagrangian
    mc         market-clearing complementarity
;

q_n.fx = 100;


** ND cost fnc
costs .. nd_costs =e= 80*q_n+0.0015*power(q_n,2) + a*p_rec*q_n - p*q_n;

*** KKTs from renewable fringe
grd_r      .. p =e=  20 + 0.001*q_r - (1-a)*p_rec;
inv_demand .. p =e= 100 - 0.01*(q_n+q_r);

mc .. (1-a)*q_r - a*q_n =g= 0;

model ndrf /costs,grd_r,inv_demand,mc.p_rec/;

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
    solve ndrf min nd_costs using mpec;
    q_r_res(i)=q_r.l; 
    q_n_res(i)=q_n.l; 
    p_rec_res(i)=p_rec.l; 
    p_res(i)=p.l; 
    nd_costsp(i)=nd_costs.l;
);

display
q_r_res,
q_n_res,
p_rec_res,
p_res,
nd_costsp
;
