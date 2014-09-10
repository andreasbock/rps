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

prod_n_raw="""e1       39.048      40.952
e2       78.095      81.905
e3      117.143     122.857
e4      156.190     163.810
e5      195.238     204.762
e6      234.286     245.714
e7      273.333     286.667
e8      312.381     327.619
e9      351.429     368.571
e10     390.476     409.524
e11     429.524     450.476
e12     468.571     491.429
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

power_price_raw="""e1       99.490      99.510
e2       98.979      99.021
e3       98.469      98.531
e4       97.958      98.042
e5       97.448      97.552
e6       96.937      97.063
e7       96.427      96.573
e8       95.916      96.084
e9       95.406      95.594
e10      94.895      95.105
e11      94.385      94.615
e12      93.874      94.126
e13      93.440      93.960
e14      93.320      93.880
e15      93.200      93.800
e16      93.080      93.720
e17      92.960      93.640
e18      92.840      93.560
e19      92.720      93.480
e20      92.600      93.400
e21      92.480      93.320
e22      92.360      93.240
e23      92.240      93.160
e24      92.120      93.080
e25      92.000      93.000
e26      91.880      92.920
e27      91.760      92.840
e28      91.640      92.760
e29      91.520      92.680
e30      91.400      92.600
e31      91.280      92.520
e32      91.160      92.440
e33      91.040      92.360
e34      90.920      92.280
e35      90.800      92.200
e36      90.680      92.120
e37      90.560      92.040
e38      90.440      91.960
e39      90.320      91.880
e40      90.200      91.800
e41      90.080      91.720
e42      89.960      91.640
e43      89.840      91.560
e44      89.720      91.480
e45      89.600      91.400
e46      89.480      91.320
e47      89.360      91.240
e48      89.240      91.160
e49      89.120      91.080
e50      89.000      91.000"""

profit_r_raw = """e1  8702377.295,    e2  1.736951E+7,    e3  2.600140E+7,    e4  3.459804E+7,    e5  4.315943E+7,    e6  5.168558E+7,    e7  6.017649E+7,    e8  6.863215E+7,    e9  7.705256E+7,    e10 8.543773E+7,    e11 9.378765E+7,    e12 1.021023E+8,    e13 1.103818E+8
e14 1.186259E+8,    e15 1.268349E+8,    e16 1.350086E+8,    e17 1.431470E+8,    e18 1.512502E+8,    e19 1.593182E+8,    e20 1.673509E+8,    e21 1.753484E+8,    e22 1.833106E+8,    e23 1.912376E+8,    e24 1.991293E+8,    e25 2.069858E+8,    e26 2.148071E+8
e27 2.225930E+8,    e28 2.303438E+8,    e29 2.380593E+8,    e30 2.457396E+8,    e31 2.533846E+8,    e32 2.609944E+8,    e33 2.685689E+8,    e34 2.761082E+8,    e35 2.836122E+8,    e36 2.910810E+8,    e37 2.985145E+8,    e38 3.059128E+8,    e39 3.132759E+8
e40 3.206037E+8,    e41 3.278962E+8,    e42 3.351535E+8,    e43 3.423756E+8,    e44 3.495624E+8,    e45 3.567140E+8,    e46 3.637998E+8,    e47 3.707904E+8,    e48 3.777420E+8,    e49 3.846545E+8,    e50 3.915280E+8"""

profit_n_raw ="""e1  8702247.103,    e2  1.736979E+7,    e3  2.600262E+7,    e4  3.460075E+7,    e5  4.316418E+7,    e6  5.169290E+7,    e7  6.018691E+7,    e8  6.864621E+7,    e9  7.707082E+7,    e10 8.546071E+7,    e11 9.381590E+7,    e12 1.021364E+8,    e13 1.104222E+8
e14 1.186732E+8,    e15 1.268896E+8,    e16 1.350713E+8,    e17 1.432182E+8,    e18 1.513305E+8,    e19 1.594080E+8,    e20 1.674508E+8,    e21 1.754590E+8,    e22 1.834324E+8,    e23 1.913711E+8,    e24 1.992751E+8,    e25 2.071444E+8,    e26 2.149790E+8
e27 2.227789E+8,    e28 2.305441E+8,    e29 2.382746E+8,    e30 2.459704E+8,    e31 2.536315E+8,    e32 2.612578E+8,    e33 2.688495E+8,    e34 2.764065E+8,    e35 2.839287E+8,    e36 2.914162E+8,    e37 2.988691E+8,    e38 3.062872E+8,    e39 3.136706E+8
e40 3.210194E+8,    e41 3.283334E+8,    e42 3.356127E+8,    e43 3.428573E+8,    e44 3.500672E+8,    e45 3.572424E+8,    e46 3.643801E+8,    e47 3.714639E+8,    e48 3.784918E+8,    e49 3.854639E+8,    e50 3.923803E+89"""

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
	i = 0
	for p_raw in profit_r_raw.split('\n'):
		for p_raw2 in p_raw.split(','):
			profit_r[i] = float(p_raw2.split()[1])
			i+=1

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

i = 0
for p_raw in prod_r_raw.split('\n'):
    p = p_raw.split()[1:]
    q_r[i] = np.array(map(float, p))
    i +=1
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

		ax2.set_ylabel(r"REC Price ($p_{REC}$)")
		#power_prices1,  = ax2.plot(x,power_price.T[0],'--',c='black')
		#power_prices2,  = ax2.plot(x,power_price.T[1],'.')
		rec_price_plot, = ax2.plot(x,rec_price,'x',c='red')
		ax.set_xlabel(r'Renewable Capacity ($w$)')
		ax.set_ylabel(r'Profit of the producers')
		if one_dim:
			profit_r_plt,= ax.plot(x,profit_r,'s')
			profit_n_plt,= ax.plot(x,profit_n)
		else:
			profit,= ax.plot(x,z.T[int(a*10)])
		#ax.legend([profit_r_plt,power_prices1,power_prices2], ["Profit","Power price, scenario 1 (high)", "Power price, scenario 2 (low)"], loc='upper center', bbox_to_anchor=(0, -0.125),fancybox=True, shadow=True, ncol=5)
		#ax.legend([profit_r_plt,profit_n_plt,power_prices1,power_prices2,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_e^1$","$p_e^2$", "$p_{REC}$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("foo.svg",bbox_inches='tight')
		exit()
	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.grid(True)
		for loc, spine in ax.spines.items():
			if loc in ['left','bottom','right']:
				spine.set_position(('outward',10)) # outward by 10 points

		ax.spines['top'].set_visible(False)
		ax.spines['bottom'].set_smart_bounds(True)
		ax.set_xlabel(r'Expected Renewable Capacity ($E_t[w^t]$)')
		ax.set_ylabel(r"Quantities ($q_r^t$, $q_n^t$)")
		q_r_plt1, = ax.plot(x,q_r.T[0],'--',c='green')
		q_r_plt2, = ax.plot(x,q_r.T[1],'.',c='green')
		q_n_plt1, = ax.plot(x,q_n.T[0],'x',c='black')
		q_n_plt2, = ax.plot(x,q_n.T[1],'k',c='black')

		ax.legend([q_r_plt1, q_r_plt2, q_n_plt1, q_n_plt2], ["$q_r^1$","$q_r^2$","$q_n^1$","$q_n^2$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("fooprod.svg",bbox_inches='tight')

