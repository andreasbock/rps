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

prod_n_raw="""e1        9.048      10.952
e2       18.095      21.905
e3       27.143      32.857
e4       36.190      43.810
e5       45.238      54.762
e6       54.286      65.714
e7       63.333      76.667
e8       72.381      87.619
e9       81.429      98.571
e10      90.476     109.524
e11      99.524     120.476
e12     108.571     131.429
e13     117.619     142.381
e14     126.667     153.333
e15     135.714     164.286
e16     144.762     175.238
e17     153.810     186.190
e18     162.857     197.143
e19     171.905     208.095
e20     180.952     219.048
e21     190.000     230.000
e22     199.048     240.952
e23     208.095     251.905
e24     217.143     262.857
e25     226.190     273.810
e26     235.238     284.762
e27     244.286     295.714
e28     253.333     306.667
e29     262.381     317.619
e30     271.429     328.571
e31     280.476     339.524
e32     289.524     350.476
e33     298.571     361.429
e34     307.619     372.381
e35     316.667     383.333
e36     325.714     394.286
e37     334.762     405.238
e38     343.810     416.190
e39     352.857     427.143
e40     361.905     438.095
e41     370.952     449.048
e42     380.000     460.000
e43     389.048     470.952
e44     398.095     481.905
e45     407.143     492.857
e46     420.000     500.000
e47     440.000     500.000
e48     460.000     500.000
e49     480.000     500.000
e50     500.000     500.000"""

power_price_raw="""e1       99.790      99.810
e2       99.579      99.621
e3       99.369      99.431
e4       99.158      99.242
e5       98.948      99.052
e6       98.737      98.863
e7       98.527      98.673
e8       98.316      98.484
e9       98.106      98.294
e10      97.895      98.105
e11      97.685      97.915
e12      97.474      97.726
e13      97.264      97.536
e14      97.053      97.347
e15      96.843      97.157
e16      96.632      96.968
e17      96.422      96.778
e18      96.211      96.589
e19      96.001      96.399
e20      95.790      96.210
e21      95.580      96.020
e22      95.370      95.830
e23      95.159      95.641
e24      94.949      95.451
e25      94.738      95.262
e26      94.528      95.072
e27      94.317      94.883
e28      94.107      94.693
e29      93.896      94.504
e30      93.686      94.314
e31      93.475      94.125
e32      93.265      93.935
e33      93.054      93.746
e34      92.844      93.556
e35      92.633      93.367
e36      92.423      93.177
e37      92.212      92.988
e38      92.002      92.798
e39      91.791      92.609
e40      91.581      92.419
e41      91.370      92.230
e42      91.160      92.040
e43      90.950      91.850
e44      90.739      91.661
e45      90.529      91.471
e46      90.280      91.320
e47      89.960      91.240
e48      89.640      91.160
e49      89.320      91.080
e50      89.000      91.000"""

profit_r_raw = """e1  8702377.295,    e2  1.736951E+7,    e3  2.600140E+7,    e4  3.459804E+7,    e5  4.315943E+7,    e6  5.168558E+7,    e7  6.017649E+7,    e8  6.863215E+7,    e9  7.705256E+7,    e10 8.543773E+7,    e11 9.378765E+7,    e12 1.021023E+8,    e13 1.103818E+8
e14 1.186259E+8,    e15 1.268349E+8,    e16 1.350086E+8,    e17 1.431470E+8,    e18 1.512502E+8,    e19 1.593182E+8,    e20 1.673509E+8,    e21 1.753484E+8,    e22 1.833106E+8,    e23 1.912376E+8,    e24 1.991293E+8,    e25 2.069858E+8,    e26 2.148071E+8
e27 2.225930E+8,    e28 2.303438E+8,    e29 2.380593E+8,    e30 2.457396E+8,    e31 2.533846E+8,    e32 2.609944E+8,    e33 2.685689E+8,    e34 2.761082E+8,    e35 2.836122E+8,    e36 2.910810E+8,    e37 2.985145E+8,    e38 3.059128E+8,    e39 3.132759E+8
e40 3.206037E+8,    e41 3.278962E+8,    e42 3.351535E+8,    e43 3.423756E+8,    e44 3.495624E+8,    e45 3.567140E+8,    e46 3.637998E+8,    e47 3.707904E+8,    e48 3.777420E+8,    e49 3.846545E+8,    e50 3.915280E+8"""

profit_n_raw ="""e1  8702247.103,    e2  1.736979E+7,    e3  2.600262E+7,    e4  3.460075E+7,    e5  4.316418E+7,    e6  5.169290E+7,    e7  6.018691E+7,    e8  6.864621E+7,    e9  7.707082E+7,    e10 8.546071E+7,    e11 9.381590E+7,    e12 1.021364E+8,    e13 1.104222E+8
e14 1.186732E+8,    e15 1.268896E+8,    e16 1.350713E+8,    e17 1.432182E+8,    e18 1.513305E+8,    e19 1.594080E+8,    e20 1.674508E+8,    e21 1.754590E+8,    e22 1.834324E+8,    e23 1.913711E+8,    e24 1.992751E+8,    e25 2.071444E+8,    e26 2.149790E+8
e27 2.227789E+8,    e28 2.305441E+8,    e29 2.382746E+8,    e30 2.459704E+8,    e31 2.536315E+8,    e32 2.612578E+8,    e33 2.688495E+8,    e34 2.764065E+8,    e35 2.839287E+8,    e36 2.914162E+8,    e37 2.988691E+8,    e38 3.062872E+8,    e39 3.136706E+8
e40 3.210194E+8,    e41 3.283334E+8,    e42 3.356127E+8,    e43 3.428573E+8,    e44 3.500672E+8,    e45 3.572424E+8,    e46 3.643801E+8,    e47 3.714639E+8,    e48 3.784918E+8,    e49 3.854639E+8,    e50 3.923803E+8"""

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
	alphas = [0.5]

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