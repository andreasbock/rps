#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

prod_r_raw="""e1       12.000       8.000
e2       24.000      16.000
e3       36.000      24.000
e4       48.000      32.000
e5       60.000      40.000
e6       72.000      48.000
e7       84.000      56.000
e8       96.000      64.000
e9      108.000      72.000
e10     120.000      80.000
e11     132.000      88.000
e12     144.000      96.000
e13     156.000     104.000
e14     168.000     112.000
e15     180.000     120.000
e16     192.000     128.000
e17     204.000     136.000
e18     216.000     144.000
e19     228.000     152.000
e20     240.000     160.000
e21     252.000     168.000
e22     264.000     176.000
e23     276.000     184.000
e24     288.000     192.000
e25     300.000     200.000
e26     312.000     208.000
e27     324.000     216.000
e28     336.000     224.000
e29     348.000     232.000
e30     360.000     240.000
e31     372.000     248.000
e32     384.000     256.000
e33     396.000     264.000
e34     408.000     272.000
e35     420.000     280.000
e36     432.000     288.000
e37     444.000     296.000
e38     456.000     304.000
e39     468.000     312.000
e40     480.000     320.000
e41     492.000     328.000
e42     504.000     336.000
e43     516.000     344.000
e44     528.000     352.000
e45     540.000     360.000
e46     552.000     368.000
e47     564.000     376.000
e48     576.000     384.000
e49     588.000     392.000
e50     600.000     400.000"""

prod_n_raw="""e1      500.000     500.000
e2      500.000     500.000
e3      500.000     500.000
e4      500.000     500.000
e5      500.000     500.000
e6      500.000     500.000
e7      500.000     500.000
e8      500.000     500.000
e9      500.000     500.000
e10     500.000     500.000
e11     500.000     500.000
e12     500.000     500.000
e13     500.000     500.000
e14     500.000     500.000
e15     500.000     500.000
e16     500.000     500.000
e17     500.000     500.000
e18     500.000     500.000
e19     500.000     500.000
e20     500.000     500.000
e21     500.000     500.000
e22     500.000     500.000
e23     500.000     500.000
e24     500.000     500.000
e25     500.000     500.000
e26     500.000     500.000
e27     500.000     500.000
e28     500.000     500.000
e29     500.000     500.000
e30     500.000     500.000
e31     500.000     500.000
e32     500.000     500.000
e33     500.000     500.000
e34     500.000     500.000
e35     500.000     500.000
e36     500.000     500.000
e37     500.000     500.000
e38     500.000     500.000
e39     500.000     500.000
e40     500.000     500.000
e41     500.000     500.000
e42     500.000     500.000
e43     500.000     500.000
e44     500.000     500.000
e45     500.000     500.000
e46     500.000     500.000
e47     500.000     500.000
e48     500.000     500.000
e49     500.000     500.000
e50     500.000     500.000"""

power_price_raw="""e1       95.000      95.000
e2       95.000      95.000
e3       95.000      95.000
e4       95.000      95.000
e5       95.000      95.000
e6       95.000      95.000
e7       95.000      95.000
e8       95.000      95.000
e9       95.000      95.000
e10      95.000      95.000
e11      95.000      95.000
e12      95.000      95.000
e13      95.000      95.000
e14      95.000      95.000
e15      95.000      95.000
e16      95.000      95.000
e17      95.000      95.000
e18      95.000      95.000
e19      95.000      95.000
e20      95.000      95.000
e21      95.000      95.000
e22      95.000      95.000
e23      95.000      95.000
e24      95.000      95.000
e25      95.000      95.000
e26      95.000      95.000
e27      95.000      95.000
e28      95.000      95.000
e29      95.000      95.000
e30      95.000      95.000
e31      95.000      95.000
e32      95.000      95.000
e33      95.000      95.000
e34      95.000      95.000
e35      95.000      95.000
e36      95.000      95.000
e37      95.000      95.000
e38      95.000      95.000
e39      95.000      95.000
e40      95.000      95.000
e41      95.000      95.000
e42      95.000      95.000
e43      95.000      95.000
e44      95.000      95.000
e45      95.000      95.000
e46      95.000      95.000
e47      95.000      95.000
e48      95.000      95.000
e49      95.000      95.000
e50      95.000      95.000"""

profit_r_raw = """e1  8676217.295,    e2  1.726487E+7,    e3  2.576596E+7,    e4  3.417948E+7,    e5  4.250543E+7,    e6  5.074382E+7,    e7  5.889465E+7,    e8  6.695791E+7,    e9  7.493360E+7,    e10 8.282173E+7,    e11 9.062229E+7,    e12 9.833529E+7,    e13 1.061594E+8
e14 1.141985E+8,    e15 1.222195E+8,    e16 1.302224E+8,    e17 1.382071E+8,    e18 1.461737E+8,    e19 1.541222E+8,    e20 1.620525E+8,    e21 1.699647E+8,    e22 1.778587E+8,    e23 1.857346E+8,    e24 1.935924E+8,    e25 2.014320E+8,    e26 2.092535E+8
e27 2.170568E+8,    e28 2.248421E+8,    e29 2.326091E+8,    e30 2.403581E+8,    e31 2.480889E+8,    e32 2.558015E+8,    e33 2.634961E+8,    e34 2.711725E+8,    e35 2.788307E+8,    e36 2.864708E+8,    e37 2.940928E+8,    e38 3.016967E+8,    e39 3.092824E+8
e40 3.168499E+8,    e41 3.243993E+8,    e42 3.319306E+8,    e43 3.394438E+8,    e44 3.469388E+8,    e45 3.544157E+8,    e46 3.618744E+8,    e47 3.693150E+8,    e48 3.767375E+8,    e49 3.841418E+8,    e50 3.915280E+8"""

profit_n_raw ="""e1  4.141802E+8,    e2  4.141802E+8,    e3  4.141802E+8,    e4  4.141802E+8,    e5  4.141802E+8,    e6  4.141802E+8,    e7  4.141802E+8,    e8  4.141802E+8,    e9  4.141802E+8,    e10 4.141802E+8,    e11 4.141802E+8,    e12 4.141802E+8,    e13 4.141802E+8
e14 4.141802E+8,    e15 4.141802E+8,    e16 4.141802E+8,    e17 4.141802E+8,    e18 4.141802E+8,    e19 4.141802E+8,    e20 4.141802E+8,    e21 4.141802E+8,    e22 4.141802E+8,    e23 4.141802E+8,    e24 4.141802E+8,    e25 4.141802E+8,    e26 4.141802E+8
e27 4.141802E+8,    e28 4.141802E+8,    e29 4.141802E+8,    e30 4.141802E+8,    e31 4.141802E+8,    e32 4.141802E+8,    e33 4.141802E+8,    e34 4.141802E+8,    e35 4.141802E+8,    e36 4.141802E+8,    e37 4.141802E+8,    e38 4.141802E+8,    e39 4.141802E+8
e40 4.141802E+8,    e41 4.141802E+8,    e42 4.141802E+8,    e43 4.141802E+8,    e44 4.141802E+8,    e45 4.141802E+8,    e46 4.141802E+8,    e47 4.141802E+8,    e48 4.141802E+8,    e49 4.141802E+8,    e50 4.141802E+8"""

rec_price_raw= """"""

# THIS DETERMINES TO USE MATRIX OR THE ARRAY PROFIT
one_dim = True

opt = str(sys.argv[1])
rc('text',usetex=True)
rc('font',family='serif')
profit_raw_split = profit_raw.split('\n')
rows = len(profit_raw_split)

if one_dim:
	profit_r = np.zeros(shape=(50))
#	i = 0
#	for p_raw in profit_r_raw.split('\n'):
#		for p_raw2 in p_raw.split(','):
#			profit_r[i] = float(p_raw2.split()[1])
#			i+=1

	profit_n = np.zeros(shape=(50))
	i = 0
	for p_raw in profit_n_raw.split('\n'):
		for p_raw2 in p_raw.split(','):
			profit_n[i] = float(p_raw2.split()[1])
			i+=1
else:
	z = np.zeros(shape=(50,11))
	i = 0
	for p_raw in profit_raw.split('\n'):
	    p = p_raw.split()[1:]
	    z[i] = np.array(map(float, p))
	    i +=1

power_price = np.zeros(shape=(50,2))

i = 0
for p_raw in power_price_raw.split('\n'):
    p = p_raw.split()[1:]
    power_price[i] = np.array(map(float, p))
    i +=1

rec_price = np.zeros(shape=(50))

#i = 0
#for p_raw in rec_price_raw.split('\n'):
#	for p_raw2 in p_raw.split(','):
#		rec_price[i] = float(p_raw2.split()[1])
#		i+=1

q_r = np.zeros(shape=(50,2))

#i = 0
#for p_raw in prod_r_raw.split('\n'):
#    p = p_raw.split()[1:]
#    q_r[i] = np.array(map(float, p))
#    i +=1
q_n = np.zeros(shape=(50,2))
i = 0
for p_raw in prod_n_raw.split('\n'):
    p = p_raw.split()[1:]
    q_n[i] = np.array(map(float, p))
    i +=1

if opt == "3d" and not one_dim:
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.set_xlabel(r'RPS ($\alpha$)')
	ax.set_ylabel(r'Average Capacity ($E[w(\omega)]$)')
	ax.set_zlabel(r'Profit of the renewable')
	rps      = np.arange(0,1.1,0.1)
	capacity = np.arange(1,51,1)
	x,y = np.meshgrid(rps,capacity)
	ax.plot_surface(x, y, z, cmap=cm.gnuplot)

	fig.savefig('foo3d.png',bbox_inches='tight')
else:
	alphas = [0.2]

	x = 10*np.arange(1,51)

	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.grid(True)
		for loc, spine in ax.spines.items():
			if loc in ['left','bottom','right']:
				spine.set_position(('outward',10)) # outward by 10 points
		ax2 = ax.twinx()
		ax.spines['top'].set_visible(False)
		ax.spines['bottom'].set_smart_bounds(True)
		ax2.spines['top'].set_visible(False)
		ax2.spines['bottom'].set_smart_bounds(True)
		for loc, spine in ax2.spines.items():
			if loc in ['left','bottom','right']:
				spine.set_position(('outward',10)) # outward by 10 points

		ax2.set_ylabel(r"Prices ($p(\omega)$, $p_{REC}$)")
		power_prices1,  = ax2.plot(x,power_price.T[0],'--',c='black')
		#print power_price.T[0]; exit()
		power_prices2,  = ax2.plot(x,power_price.T[1],'.')
		rec_price_plot, = ax2.plot(x,rec_price,'x')
		ax.set_xlabel(r'Average Renewable Capacity ($E[w(\omega)]$)')
		ax.set_ylabel(r'Profit of the producers')
		if one_dim:
			profit_r_plt,= ax.plot(x,profit_r,'s')
			profit_n_plt,= ax.plot(x,profit_n)
		else:
			profit,= ax.plot(x,z.T[int(a*10)])
		#ax.legend([profit_r_plt,power_prices1,power_prices2], ["Profit","Power price, scenario 1 (high)", "Power price, scenario 2 (low)"], loc='upper center', bbox_to_anchor=(0, -0.125),fancybox=True, shadow=True, ncol=5)
		ax.legend([profit_r_plt,profit_n_plt,power_prices1,power_prices2,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_e^1$","$p_e^2$", "$p_{REC}$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("foo.svg",bbox_inches='tight')

	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		for loc, spine in ax.spines.items():
			if loc in ['left','bottom','right']:
				spine.set_position(('outward',10)) # outward by 10 points

		ax.spines['top'].set_visible(False)
		ax.spines['bottom'].set_smart_bounds(True)
		ax.grid(True)
		ax.set_xlabel(r'Expected Renewable Capacity ($E_t[w^t]$)')
		ax.set_ylabel(r"Quantities ($q_r^t$, $q_n^t$)")
		q_r_plt1, = ax.plot(x,q_r.T[0],'--',c='green')
		q_r_plt2, = ax.plot(x,q_r.T[1],'.',c='green')
		q_n_plt1, = ax.plot(x,q_n.T[0],'x',c='black')
		q_n_plt2, = ax.plot(x,q_n.T[1],'k',c='black')

		ax.legend([q_r_plt1, q_r_plt2, q_n_plt1, q_n_plt2], ["$q_r^1$","$q_r^2$","$q_n^1$","$q_n^2$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("fooprod.svg",bbox_inches='tight')