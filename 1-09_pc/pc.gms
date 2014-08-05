option mcp=path;

parameter
    a        RPS requirement
;

variables
    nd_costs negative profit of the non-renewable
    p        electricity price
    p_rec    price of RECs
    q_r     renewable generation
    q_n     non-renewable generation
    gamma_r_lo
    gamma_n_lo
;

positive variable p_rec;
positive variables gamma_r_lo, gamma_n_lo;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r      gradient over R lagrangian
    grd_n      gradient over N lagrangian
    mcc        market-clearing complementarity
    min_n      minimum productino for N
    min_r      minimum productino for R
;

** Non-renewable Gradient
grd_n .. p =e= 20 + 0.001*q_n + a*p_rec*q_n - gamma_n_lo;
*grd_n .. p =e= 20 + 0.001*q_n + a*p_rec*q_n;
min_n .. q_n =g= 0;

** Renewable Gradient
grd_r .. p =e= 80 + 0.003*q_r - (1-a)*p_rec - gamma_r_lo;
*grd_r .. p =e= 80 + 0.003*q_r - (1-a)*p_rec;
min_r .. q_r =g= 0;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);
mcc .. (1-a)*q_r - a*q_n =g= 0;


model pc
/grd_n,
grd_r,
inv_demand,
mcc.p_rec
min_n.gamma_n_lo,
min_r.gamma_r_lo
/;

pc.optfile = 1;

a=1.0;
solve pc using mcp;

display
q_r.l,
q_n.l,
p_rec.l,
p.l
;
$exit

*** Loop over all RPS levels
set i /i1*i11/;

parameter q_r_res(i);
parameter q_n_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_rf(i);
parameter profits_nd(i);

loop(i,
    a=(ord(i)-1)/10;
    solve pc using mcp;
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
