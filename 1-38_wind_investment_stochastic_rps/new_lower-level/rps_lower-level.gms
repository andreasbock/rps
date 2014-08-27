parameter
a   /0/
d /500/
;

variables
z
q_r
q_n
p_rec
;

equations
obj
max_r
min_r
max_n
min_n
demand
;

obj .. z =e= 20*q_n + 0.0005*power(q_n,2) - (1-a)*p_rec*q_r + a*p_rec*q_n;

max_r .. q_r =l= 300;
min_r .. 0   =l= q_r;

max_n .. q_n =l= 500;
min_n .. 0   =l= q_n;

demand .. d - (q_r+q_n) =e= 0;

model ll /all/;
solve ll using miqcp min z;
