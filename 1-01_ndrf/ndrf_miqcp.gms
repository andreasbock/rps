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

scalar M constant for Fortuny-Amat linearization /10000000/;

variables
    nd_costs profit of the non-renewable dominant
    p        electricity price
    p_rec    price of RECs
    q_rf     renewable generation in stage t
    u_mc     linearization of REC market-clearing
*   profit_rf 
*   profit_nd
;

scalar result /0/;

positive variables q_nd, q_rf, p, p_rec;
binary variables u_mc;
equations
    costs objective function
    inv_demand   inverse demand function
    grd_rf       gradient over RF lagrangian
*    cs_rf_lo_a complementary slackness for RF
*    cs_rf_lo_b complementary slackness for RF
*    cs_rf_hi_a complementary slackness for RF
*    cs_rf_hi_b complementary slackness for RF
*    cs_rf_hi_c complementary slackness for RF
    mc_a    market-clearing complementarity
    mc_b    market-clearing complementarity
    mc_c    market-clearing complementarity
*    profit_rf_c profit of the fringe
*    profit_nd_c profit of the dominant firm
;

** ND cost fnc
costs .. nd_costs =e= 20*q_nd+0.0005*power(q_nd,2) + a*p_rec*q_nd - p*q_nd;

*** KKTs from renewable fringe
grd_rf     .. p =e=  80 + 0.003*q_rf - (1-a)*p_rec;
inv_demand .. p =e= 100 - 0.01*(q_nd+q_rf);

mc_a .. (1-a)*q_rf - a*q_nd =l= M*u_mc;
mc_b .. p_rec               =l= M*(1-u_mc);
mc_c .. (1-a)*q_rf - a*q_nd =g= 0;

*profit_rf_c .. profit_rf =e= p*q_rf + (1-a)*p_rec*q_rf;
*profit_nd_c .. profit_nd =e= -nd_costs;

model ndrf /all/;

*** Loop over all RPS levels
set i /i1*i11/;

parameter q_rf_res(i);
parameter q_nd_res(i);
parameter p_rec_res(i);
parameter p_res(i);
parameter profits_rf(i);
parameter profits_nd(i);
parameter nd_costsp(i);

loop(i,
    a=(ord(i)-1)/10;
    solve ndrf min nd_costs using miqcp;
    q_rf_res(i)=q_rf.l; 
    q_nd_res(i)=q_nd.l; 
    p_rec_res(i)=p_rec.l; 
    p_res(i)=p.l; 
    nd_costsp(i)=nd_costs.l;
*   profits_rf(i) = profit_rf.l;
*   profits_nd(i) = profit_nd.l;
);

display
q_rf_res,
q_nd_res,
p_rec_res,
p_res,
nd_costsp
;

result = 20*q_nd.l+0.0005*power(q_nd.l,2) + 0.2*p_rec.l*q_nd.l - p.l*q_nd.l;
display result;
$exit
