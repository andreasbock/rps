parameter
    a        RPS requirement
    cp       compliance payment /100/
;

variables
    nd_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_r      renewable generation
    q_n      non-renewable generation
    u        setting p_rec in interval
    dummy    dummy for cp-p_rec
;

positive variable u;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r      gradient over R lagrangian
    grd_n      gradient over N lagrangian
    mc_a       market-clearing complementarity
    mc_b       market-clearing complementarity
    p_rec_disc discretise p_rec
    dummy_c
    u_c
;

**** Non-renewable Gradient
*grd_n .. p =e= 20 + 0.001*q_n + a*p_rec*q_n;
*
*** Renewable Gradient
*grd_r .. p =e= 80 + 0.003*q_r - (1-a)*p_rec;
*inv_demand .. p =e= 100 - 0.01*(q_n+q_r);
*
*mc_a .. (1-a)*q_r - a*q_n =g= 0;
*mc_b .. cp - p_rec =g= 0;
*p_rec_disc .. p_rec =e= cp*u;
*
*dummy_c .. dummy =e= cp - p_rec;
*dummy_c .. p_rec =e= cp*u;
*u_c .. 1-u =g= 0;

*** Non-renewable Gradient
*grd_n .. p =e= 20 + 0.001*q_n + a*cp*u*q_n;
grd_n .. p =e= 20 + 0.001*q_n + a*p_rec*q_n;

** Renewable Gradient
grd_r .. p =e= 80 + 0.003*q_r - (1-a)*p_rec;
inv_demand .. p =e= 100 - 0.01*(q_n+q_r);

mc_a .. (1-a)*q_r - a*q_n =g= 0;
mc_b .. cp - cp*u =g= 0;
*cp*u_disc .. cp*u =e= cp*u;

*dummy_c .. dummy =e= cp - p_rec;
dummy_c .. p_rec =e= cp*u;
u_c .. 1-u =g= 0;

model pc
/grd_n,
grd_r,
inv_demand,
*p_rec_disc,
*mc_b,
mc_a.u,
dummy_c
*u_c
/;

*** Loop over all RPS levels
set i /i1*i11/;

parameter q_r_res(i);
parameter q_n_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_rf(i);
parameter profits_nd(i);
parameter ul(i);

loop(i,
    a=(ord(i)-1)/10;
    solve pc using mcp;
    q_r_res(i)=q_r.l; 
    q_n_res(i)=q_n.l; 
    ul(i)=u.l;
*   p_rec_res(i)=p_rec.l; 
    p_rec_res(i)=cp*u.l;
*   p_res(i)=p.l; 
    p_res(i)=100-0.01*(q_n.l+q_r.l);
);

display
q_r_res,
q_n_res,
*ul,
p_rec_res,
p_res
;
