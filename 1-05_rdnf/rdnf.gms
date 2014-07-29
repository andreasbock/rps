*--- RD-NF Model
$offlisting

parameter
    a        RPS requirement
;

variables
    r_costs profit of the renewable
    p        electricity price
    p_rec    price of RECs
    q_n      non-renewable generation
    q_r      renewable generation
;

positive variables q_n, q_r, p, p_rec;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_n      FO condition for non-renewable
    mc         market-clearing complementarity
;

** ND cost fnc
costs .. r_costs =e= 80*q_r+0.0015*power(q_r,2) -(1-a)*p_rec*q_r - p*q_r;

*** KKTs from renewable fringe
grd_n      .. p =e= 20 + 0.001*q_n + a*p_rec;
inv_demand .. p =e= 100 - 0.01*(q_n+q_r);

mc .. (1-a)*q_r - a*q_n =g= 0;

model rdnf /costs,grd_n,inv_demand,mc.p_rec/;

*** Loop over all RPS levels
set i /i1*i11/;

parameter q_r_res(i);
parameter q_n_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_r(i);
parameter profits_n(i);

loop(i,
    a=(ord(i)-1)/10;
    solve rdnf min r_costs using mpec;
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
