*-- Stochastic Wind power investment --*

$offlisting

Sets
    s   scenarios /s0, s1/
    b   binary for expansion block discretisation /1*1000/
    a_range  levels of RPS   /a0*a10/
    p_rec_range  levels of RPS   /p0*p20/
;

Scalar
    a      RPS requirement
    n_min  minimum non-renewable production /0/
    n_max  maximum non-renewable production /600/
    exp_bl renewable expansion blocks       /100/
    c_inv  investment cost per unit         /5/
    c_max  investment budget                /3000/
    d      demand for electricity           /600/
    M      constant                         /100000000/
    p_rec  REC price
;

Parameter
    w(s)      wind production           /s0 1.5, s1 0.9/
    p(s)      probability of scenario s /s0 0.5, s1 0.5/
;

Variables
    r_costs objective function value
    q_r(s)  renewable generation
    q_n(s)  non-renewable generation
    r_inst  renewable capacity installed
    lda(s)  demand dual
    v(b)    binary
* Dual variables
    gam_r_lo(s)
    gam_r_hi(s)
    gam_n_lo(s)
    gam_n_hi(s)
* Used in linearization
    k(b,s)
    k_hat(b,s)
    u_n_hi(s)
    u_n_lo(s)
    u_r_hi(s)
    u_r_lo(s)
    u_mcc
    mz
;

*positive variable p_rec;
positive variable q_r, q_n;
positive variable r_inst;
positive variable gam_r_lo, gam_r_hi, gam_n_lo, gam_n_hi;
positive variable lda;

binary variable v, u_n_hi, u_n_lo, u_r_hi, u_r_lo, u_mcc;

Equations
    obj       negative profits for renewable
    inv_disc  discretise the investment size
    inv_bound upper bound on investment size

    grd_lg_r    gradient over renewable lagrangian
    grd_lg_n    gradient over non-renewable lagrangian
    primal_dual primal-dual for lower-level
    demand      balance equation
    n_up_a
    n_up_b
    n_up_c
    n_lo_a
    n_lo_b

    r_up_a
    r_up_b
    r_up_c
    r_lo_a
    r_lo_b
    
    mcc_a
    mcc_b
    mcc_c

    lin_lda1_1
    lin_lda1_2
    lin_lda2_1
    lin_lda2_2
    set_k

    prim
    dual
    mcc_r
;

* Upper-level problem
obj .. r_costs =e= c_inv*r_inst
                 - exp_bl*sum(s,p(s)*w(s)*sum(b,k(b,s)))
                 - (1-a)*p_rec*sum(s,p(s)*q_r(s));

inv_disc .. r_inst =e= exp_bl*sum(b,v(b));
inv_bound .. c_inv*r_inst =l= c_max;

* KKTs for lower-level problem
grd_lg_r(s) ..                 - gam_r_lo(s) + gam_r_hi(s) - lda(s) =e= 0;
grd_lg_n(s) .. 20+0.001*q_n(s) - gam_n_lo(s) + gam_n_hi(s) - lda(s) =e= 0;
demand(s)   .. d - (q_r(s) + q_n(s)) =e= 0;

n_up_a(s) .. n_max - q_n(s) =l= M*u_n_hi(s);
n_up_b(s) .. gam_n_hi(s)    =l= M*(1-u_n_hi(s));
n_up_c(s) .. q_n(s) =l= n_max;

n_lo_a(s) .. q_n(s)      =l= M*u_n_lo(s);
n_lo_b(s) .. gam_n_lo(s) =l= M*(1-u_n_lo(s));

r_up_a(s) .. w(s)*r_inst - q_r(s) =l= M*u_r_hi(s);
r_up_b(s) .. gam_r_hi(s)          =l= M*(1-u_r_hi(s));
r_up_c(s) .. q_r(s)               =l= w(s)*r_inst;

r_lo_a(s) .. q_r(s)      =l= M*u_r_lo(s);
r_lo_b(s) .. gam_r_lo(s) =l= M*(1-u_r_lo(s));

*** Market-clearing of certificates
mcc_a .. sum(s, p(s)*((1-a)*q_r(s) - a*q_n(s))) =g= 0;
mcc_b .. sum(s, p(s)*((1-a)*q_r(s) - a*q_n(s))) =l= M*u_mcc;
mcc_c .. p_rec =l= M*(1-u_mcc);

* Linearizing lambda term in objective
set_k(b,s)      .. k(b,s) =e= gam_r_hi(s) - k_hat(b,s);
lin_lda1_1(b,s) .. 0 =l= k(b,s);
lin_lda1_2(b,s) .. k(b,s) =l= v(b)*M;
lin_lda2_1(b,s) .. 0 =l= k_hat(b,s);
lin_lda2_2(b,s) .. k_hat(b,s) =l= (1-v(b))*M;

mcc_r .. mz =e= sum(s, p(s)*((1-a)*q_r(s) - a*q_n(s)));

model stoch_wind_exp
/obj,
inv_disc,
inv_bound,
grd_lg_r,
grd_lg_n,
demand,
n_up_a,
n_up_b,
n_up_c,
n_lo_a,
n_lo_b,
r_up_a,
r_up_b,
r_up_c,
r_lo_a,
r_lo_b,
mcc_a,
mcc_b,
mcc_c,
lin_lda1_1,
lin_lda1_2,
lin_lda2_1,
lin_lda2_2,
set_k,
mcc_r
/;

*a = 1;
*p_rec = p_rec_param('i10');
*solve stoch_wind_exp min r_costs using mip;
*display q_r.l;
*display q_n.l;
*display r_inst.l;
*display r_costs.l;
*$exit

parameter q_r_res(a_range,s);
parameter q_n_res(a_range,s);
parameter lda_res(a_range,s);
parameter r_inst_res(a_range);
parameter r_costs_res(a_range);
parameter p_rec_res(a_range);
parameter mcc_rhs_res(a_range);

scalar    prev_r_costs;

loop(a_range,
    prev_r_costs = INF;

    loop(p_rec_range,
        a     = (ord(a_range)-1)/10;
        p_rec = (ord(p_rec_range)-1)*1000;
    
        solve stoch_wind_exp min r_costs using mip;

        if (r_costs.l < prev_r_costs,
            prev_r_costs = r_costs.l;

            q_r_res(a_range,s) = q_r.l(s);
            q_n_res(a_range,s) = q_n.l(s);
            lda_res(a_range,s) = lda.l(s);
            r_inst_res(a_range) = r_inst.l;
            r_costs_res(a_range) = r_costs.l;
            p_rec_res(a_range) = p_rec;
            mcc_rhs_res(a_range) = sum(s, p(s)*((1-a)*q_r.l(s) - a*q_n.l(s)));
        );
    );
);

display
r_costs_res,
p_rec_res,
q_r_res,
q_n_res,
r_inst_res,
lda_res,
mcc_rhs_res
;



