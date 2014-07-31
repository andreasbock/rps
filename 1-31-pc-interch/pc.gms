parameter
    a        RPS requirement
;

variables
    nd_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_r     renewable generation
    q_n     non-renewable generation
;

positive variables p_rec;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r     gradient over R lagrangian
    grd_n     gradient over N lagrangian
    mcc         market-clearing complementarity
;

** Non-renewable Gradient
grd_n .. p =e= 80 + 0.003*q_n + a*p_rec*q_n;

** Renewable Gradient
grd_r .. p =e= 20 + 0.001*q_r - (1-a)*p_rec;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);
mcc .. (1-a)*q_r - a*q_n =g= 0;

model pc /grd_n,grd_r,inv_demand,mcc.p_rec/;

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
