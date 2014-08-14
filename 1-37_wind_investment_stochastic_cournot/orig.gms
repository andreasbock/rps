*-- Stochastic Wind power investment --*

Sets
    nb /1*1000/
    g /g1,g2,g3,g4/
    gn1(g) /g2,g3,g4/
    w /w1,w2,w3/;

alias(gs,g);
alias(ws,w);

Scalar
    ig1 /50000/
    ig1_cap /1000/
    ig1_block /1/
    M1 /1000000/
    M2 /100000/
    M3 /10000/
    M4 /10000/
    M5 /10000/
    M6 /10000/;

Parameter
    c(g) /g1 5, g2 7, g3 10, g4 15/
    t(w) /w1 2920, w2 2920, w3 2920/
    d(w) /w1 325, w2 575, w3 750/
    maxp(g) maximum production /g2 25, g3 400, g4 400/
    minp(g) maximum production /g1 0, g2 0, g3 0, g4 0/;

*Parameter
*    c(g) /g1 5, g2 7, g3 10, g4 15/
*    t(w) /w1 2920, w2 2920, w3 2920/
*    d(w) /w1 325, w2 575, w3 750/
*    maxp(g) maximum production /g2 25, g3 400, g4 400/
*    minp(g) maximum production /g1 0, g2 0, g3 0/;
*
Variables
    z objective fnc value
    lda(w) demand dual
    v(nb) binary
    x(g,w) production
* Dual
    xg1_bar
    etalo(g,w)
    etahi(g,w)
* Used in linearization
    u_lo(g,w)
    u_hi(g,w)
    k(nb,g,w)
    k_hat(nb,g,w)
    primv(w)
    dualv(w)
;

Positive variable x;
Positive variable etalo;
Positive variable etahi;
Positive variable xg1_bar;
Positive variable lda;
Binary variable v;
Binary variable u_lo;
Binary variable u_hi;

Equations
    obj   obj fnc
    maxg_install1 maximum installation limit
    maxg_install2 maximum installation limit sum of binary*continuous
    grd gradient over the lagrangian
    maxgenbound primal feasibility
    lin_lda1_1
    lin_lda1_2
    lin_lda2_1
    lin_lda2_2
    set_k
    max1
    primvz
    dualvz
    primaldual
    market_clearing(w);

obj .. z =e= sum(w, t(w)*(c('g1')*x('g1',w)
       + etalo('g1',w)*minp('g1') - ig1_block*sum(nb,k(nb,'g1',w)) - c('g1')*x('g1',w)
      ))
    + ig1*xg1_bar;

grd(g,w) .. c(g) + etahi(g,w) - etalo(g,w) - lda(w) =e= 0;

maxg_install1 .. ig1_cap =g= xg1_bar ;
maxg_install2 .. xg1_bar =e= sum(nb,v(nb)*ig1_block);

* KKTs
maxgenbound(gn1,w) .. maxp(gn1) - x(gn1,w) =g= 0;
max1(w) .. xg1_bar - x('g1',w) =g= 0;
market_clearing(w) .. sum(g,x(g,w)) =e= d(w);

primaldual(w) .. sum(gn1,etahi(gn1,w)*maxp(gn1)) + ig1_block*sum(nb,k(nb,'g1',w)) - d(w)*lda(w) =e= -sum(g,c(g)*x(g,w));
primvz(w) .. primv(w) =e= sum(g,c(g)*x(g,w));
dualvz(w) .. dualv(w) =e= sum(gn1,etahi(gn1,w)*maxp(gn1)) + ig1_block*sum(nb,k(nb,'g1',w)) - d(w)*lda(w);

* Linearizing lambda term in objective
lin_lda1_1(nb,w) .. 0 =l= k(nb,'g1',w);
lin_lda1_2(nb,w) .. k(nb,'g1',w) =l= v(nb)*M5;
lin_lda2_1(nb,w) .. 0 =l= k_hat(nb,'g1',w);
lin_lda2_2(nb,w) .. k_hat(nb,'g1',w) =l= (1-v(nb))*M6;
set_k(nb,w) .. k(nb,'g1',w) =e= etahi('g1',w) -  k_hat(nb,'g1',w);

Model ex5_3 /all/;
ex5_3.optcr=0;
Solve ex5_3 using mip min z;

display x.l;
display z.l;
display xg1_bar.l;
display lda.l;
display etahi.l;
display etalo.l;

display primv.l;
display dualv.l;

