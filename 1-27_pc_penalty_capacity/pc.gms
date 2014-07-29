parameter
    a        RPS requirement
    cp       compliance payment /100/
    n_max    N max gen          /2000/
    n_min    N min gen          /0/
    w        wind power         /2000/
;

variables
    nd_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_r      renewable generation
    q_n      non-renewable generation
    u        binary for setting p_rec
    dummy    dummy for cp-p_rec
    eta_r_lo dual of R min generation constraint
    eta_r_hi dual of R max generation constraint
    eta_n_lo dual of N min generation constraint
    eta_n_hi dual of N max generation constraint
;

positive variables eta_nd_lo, eta_nd_hi;
positive variables eta_rf_lo, eta_rf_hi;
*positive variables p_rec, p;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r      gradient over R lagrangian
    grd_n      gradient over N lagrangian
    min_gen_n minimum generation
    max_gen_n maximum generation
    min_gen_r minimum generation
    max_gen_r maximum generation
    mc_a       market-clearing complementarity
    mc_b       market-clearing complementarity
    p_rec_disc discretise p_rec
    dummy_c
;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);

grd_n .. p =e= eta_n_hi - eta_n_lo + 20 + 0.001*q_n + a*p_rec*q_n;
grd_r .. p =e= 80 + 0.003*q_r - (1-a)*p_rec + eta_r_hi - eta_r_lo;

max_gen_r .. w - q_r =g= 0;
min_gen_r .. q_r =g= 0;
max_gen_n .. n_max - q_n =g= 0;
min_gen_n .. q_n - n_min =g= 0;

mc_a .. (1-a)*q_r - a*q_n =g= 0;
mc_b .. cp - p_rec =g= 0;
p_rec_disc .. p_rec =e= cp*u;

dummy_c .. dummy =e= cp - p_rec;

model pc
/grd_n,
grd_r,
max_gen_r.eta_r_hi,
min_gen_r.eta_r_lo,
max_gen_n.eta_n_hi,
min_gen_n.eta_n_lo,
inv_demand,
*p_rec_disc,
mc_a.dummy,
dummy_c
/;

a=0;
solve pc using mcp;
exit;

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
