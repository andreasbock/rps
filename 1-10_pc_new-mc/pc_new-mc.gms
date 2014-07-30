*-------------------------*
*------ ND-RF Model ------*
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

scalar M constant for Fortuny-Amat linearization /4000/;

variables
    nd_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_r     renewable generation
    q_n     non-renewable generation
;

positive variables p_rec;
binary variables u_mc;

equations
    costs      objective function
    inv_demand inverse demand function
    grd_r     gradient over R lagrangian
    grd_n     gradient over N lagrangian
    mcc         market-clearing complementarity
;

** Non-renewable Gradient
grd_n .. p =e= 20 + 0.001*q_n + a*p_rec*q_n;

** Renewable Gradient
grd_r .. p =e= -(1-a)*p_rec;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);
mcc .. (1-a)*q_r - a*q_n =g= 0;

model tanaka_compl /grd_n,grd_r,inv_demand,mcc.p_rec/;

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
    solve tanaka_compl using mcp;
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

$exit
