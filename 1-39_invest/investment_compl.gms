set b_n /bn1*bn60/;
set b_r /br1*br30/;

parameters
	c_n /50/
	c_r /50/

	c_n_max /500/
	c_r_max /300/

	a
;

variables
	p
	p_rec

	q_n
	q_r

	X_n
	X_r

	u_n(b_n)
	u_r(b_r)

	eta_r_lo
	eta_r_hi

	eta_n_lo
	eta_n_hi

	phi_n
	phi_r
	
	delta_n
	delta_r

	nu_n_lo(b_n)
	nu_n_hi(b_n)

	nu_r_lo(b_r)
	nu_r_hi(b_r)
;

positive variables eta_r_lo, eta_r_hi;
positive variables eta_n_lo, eta_n_hi;
positive variables nu_r_lo, nu_r_hi;
positive variables nu_n_lo, nu_n_hi;
positive variables delta_n, delta_r;

equations
	grd_n_a
	grd_n_b
	grd_n_c

	grd_r_a
	grd_r_b
	grd_r_c

	min_r
	max_r

	min_n
	max_n

	disc_r
	disc_n

	n_bound
	r_bound

	bin_r_lo
	bin_r_hi

	bin_n_lo
	bin_n_hi

	inv_demand
	mcc
;

grd_n_a .. p =e= 20 + 0.001*q_n + a*p_rec + 0.01*q_n - eta_n_lo + eta_n_hi;
grd_n_b .. c_n - eta_n_hi + delta_n + phi_n =e= 0;
grd_n_c(b_n) .. - phi_n - nu_n_lo(b_n) + nu_n_hi(b_n) =e= 0;

grd_r_a .. p =e= -(1-a)*p_rec + 0.01*q_r - eta_r_lo + eta_r_hi;
grd_r_b .. c_r - eta_r_hi + delta_r + phi_r =e= 0;
grd_r_c(b_r) .. - phi_r - nu_r_lo(b_r) + nu_r_hi(b_r) =e= 0;

min_n  .. q_n =g= 0;
max_n  .. X_n =g= q_n;
disc_n .. sum(b_n,u_n(b_n)) - X_n =e= 0;
bin_r_lo(b_r) .. u_r(b_r) =g= 0;
bin_r_hi(b_r) .. 1 - u_r(b_r) =g= 0;
r_bound .. c_r_max - X_r =g= 0;

min_r  .. q_r =g= 0;
max_r  .. X_r =g= q_r;
disc_r .. sum(b_r,u_r(b_r)) - X_r =e= 0;
bin_n_lo(b_n) .. u_n(b_n) =g= 0;
bin_n_hi(b_n) .. 1 - u_n(b_n) =g= 0;
n_bound .. c_n_max - X_n =g= 0;

inv_demand .. p =e= 100 - 0.01*(q_n+q_r);
mcc .. (1-a)*q_r - a*q_n =g= 0;

model compl_invest
/
grd_n_a,
grd_n_b,
grd_n_c,
grd_r_a,
grd_r_b,
grd_r_c,
min_r.eta_r_lo,
max_r.eta_r_hi,
min_n.eta_n_lo,
max_n.eta_n_hi,
disc_n.phi_n,
disc_r.phi_r,
bin_r_lo.nu_r_lo,
bin_r_hi.nu_r_hi,
bin_n_lo.nu_n_lo,
bin_n_hi.nu_n_hi,
r_bound.delta_r,
n_bound.delta_n,
inv_demand,
mcc.p_rec
/;

a=0.4;
solve compl_invest using mcp;

display
q_r.l,
q_n.l,
X_r.l,
X_n.l
;






