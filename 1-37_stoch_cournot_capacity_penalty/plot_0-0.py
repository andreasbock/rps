#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  6732452.000,    e2  1.339541E+7,    e3  1.998887E+7,    e4  2.651283E+7,    e5  3.296730E+7,    e6  3.935227E+7,    e7  4.566775E+7,    e8  5.191373E+7,    e9  4.048471E+7,    e10 3.324520E+7,    e11 3.618749E+7,    e12 3.906029E+7,    e13 4.186359E+7
e14 4.459739E+7,    e15 4.726170E+7,    e16 4.985651E+7,    e17 5.238183E+7,    e18 5.483765E+7,    e19 5.722397E+7,    e20 5.954080E+7,    e21 6.178813E+7,    e22 6.396597E+7,    e23 6.607431E+7,    e24 6.811315E+7,    e25 7.008250E+7,    e26 7.198235E+7
e27 7.381271E+7,    e28 7.557357E+7,    e29 7.726493E+7,    e30 7.888680E+7,    e31 8.043917E+7,    e32 8.192205E+7,    e33 8.333543E+7,    e34 8.467931E+7,    e35 8.595370E+7,    e36 8.715859E+7,    e37 8.829399E+7,    e38 8.935989E+7,    e39 9.035629E+7
e40 9.128320E+7,    e41 9.214061E+7,    e42 9.292853E+7,    e43 9.297987E+7,    e44 9.293164E+7,    e45 9.286502E+7,    e46 9.278000E+7,    e47 9.267659E+7,    e48 9.255478E+7,    e49 9.241457E+7,    e50 9.225597E+7,    e51 9.207897E+7,    e52 9.188358E+7
e53 9.166979E+7,    e54 9.143760E+7,    e55 9.118702E+7,    e56 9.091804E+7,    e57 9.063067E+7,    e58 9.032490E+7,    e59 9.000073E+7,    e60 8.965817E+7,    e61 8.929721E+7,    e62 8.891786E+7,    e63 8.852011E+7,    e64 8.810396E+7,    e65 8.766942E+7
e66 8.721648E+7,    e67 8.674515E+7,    e68 8.625542E+7,    e69 8.574729E+7,    e70 8.522077E+7,    e71 8.430194E+7,    e72 8.330194E+7,    e73 8.230194E+7,    e74 8.130194E+7,    e75 8.030194E+7"""

profit_n_raw ="""e1  1.524668E+8,    e2  1.495416E+8,    e3  1.466454E+8,    e4  1.437781E+8,    e5  1.409398E+8,    e6  1.381305E+8,    e7  1.353501E+8,    e8  1.325987E+8,    e9  1.522409E+8,    e10 1.630128E+8,    e11 1.600075E+8,    e12 1.570313E+8,    e13 1.540839E+8
e14 1.511656E+8,    e15 1.482762E+8,    e16 1.454157E+8,    e17 1.425842E+8,    e18 1.397817E+8,    e19 1.370081E+8,    e20 1.342635E+8,    e21 1.315479E+8,    e22 1.288612E+8,    e23 1.262034E+8,    e24 1.235746E+8,    e25 1.209748E+8,    e26 1.184039E+8
e27 1.158620E+8,    e28 1.133491E+8,    e29 1.108651E+8,    e30 1.084100E+8,    e31 1.059840E+8,    e32 1.035868E+8,    e33 1.012187E+8,    e34 9.887945E+7,    e35 9.656920E+7,    e36 9.428791E+7,    e37 9.203557E+7,    e38 8.981220E+7,    e39 8.761777E+7
e40 8.545231E+7,    e41 8.331581E+7,    e42 8.120826E+7,    e43 8.016958E+7,    e44 7.926204E+7,    e45 7.836216E+7,    e46 7.746994E+7,    e47 7.658540E+7,    e48 7.570851E+7,    e49 7.483929E+7,    e50 7.397774E+7,    e51 7.312385E+7,    e52 7.227763E+7
e53 7.143907E+7,    e54 7.060818E+7,    e55 6.978495E+7,    e56 6.896939E+7,    e57 6.816149E+7,    e58 6.736126E+7,    e59 6.656869E+7,    e60 6.578379E+7,    e61 6.500656E+7,    e62 6.423699E+7,    e63 6.347508E+7,    e64 6.272084E+7,    e65 6.197427E+7
e66 6.123536E+7,    e67 6.050411E+7,    e68 5.978053E+7,    e69 5.906462E+7,    e70 5.835637E+7,    e71 5.823291E+7,    e72 5.823291E+7,    e73 5.823291E+7,    e74 5.823291E+7,    e75 5.823291E+7"""

rec_price_raw= """e1 50.000,    e2 50.000,    e3 50.000,    e4 50.000,    e5 50.000,    e6 50.000,    e7 50.000,    e8 50.000,    e9 18.400"""

# THIS DETERMINES TO USE MATRIX OR THE ARRAY PROFIT
one_dim = True

opt = str(sys.argv[1])
rc('text',usetex=True)
rc('font',family='serif')
profit_raw_split = profit_raw.split('\n')
rows = len(profit_raw_split)

if one_dim:
	profit_r = np.zeros(shape=(80))
	i = 0
	for p_raw in profit_r_raw.split('\n'):
		for p_raw2 in p_raw.split(','):
			profit_r[i] = float(p_raw2.split()[1])
			i+=1


	profit_n = np.zeros(shape=(80))
	i = 0
	for p_raw in profit_n_raw.split('\n'):
		for p_raw2 in p_raw.split(','):
			profit_n[i] = float(p_raw2.split()[1])
			i+=1
else:
	z = np.zeros(shape=(80,11))
	i = 0
	for p_raw in profit_raw.split('\n'):
	    p = p_raw.split()[1:]
	    z[i] = np.array(map(float, p))
	    i +=1

rec_price = np.zeros(shape=(80))
i=0
for p_raw in rec_price_raw.split('\n'):
	for p_raw2 in p_raw.split(','):
		rec_price[i] = float(p_raw2.split()[1])
		i+=1

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

	x = 10*np.arange(1,81)

	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		#ax.grid(True)
		for loc, spine in ax.spines.items():
			if loc in ['left','bottom','right']:
				spine.set_position(('outward',10)) # outward by 10 points
			if loc in ['top']:
				spine.set_position(('outward',15)) # outward by 10 points

		ax2 = ax.twinx()
		ax.spines['top'].set_visible(True)
		ax.spines['bottom'].set_smart_bounds(True)
		ax2.spines['top'].set_visible(True)
		ax2.spines['bottom'].set_smart_bounds(True)
		for loc, spine in ax2.spines.items():
			if loc in ['left','bottom','right']:
				spine.set_position(('outward',10)) # outward by 10 points
			if loc in ['top']:
				spine.set_position(('outward',15)) # outward by 10 points

		#ax2.set_ylabel(r'REC Price (\euro)') u"\u20AC"
		rc('text.latex', unicode=True) 
		ax2.set_ylabel(u"REC Price (\u20AC)")
		#power_prices1,  = ax2.plot(x,power_price.T[0],'--',c='black')
		#print power_price.T[0]; exit()
		#power_prices2,  = ax2.plot(x,power_price.T[1],'.')
		rec_price_plot, = ax2.plot(x,rec_price,'-',linewidth=2,c='black')
		ax.set_xlabel(r"Renewable Capacity (MW)")
		ax.set_ylabel(u"Profit of the producers (\u20AC)")
		if one_dim:
			profit_r_plt,= ax.plot(x,profit_r,'--',linewidth=4, c='black')
			profit_n_plt,= ax.plot(x,profit_n,'-.',linewidth=2, c='black')
		else:
			profit,= ax.plot(x,z.T[int(a*10)])
		#ax.legend([profit_r_plt,power_prices1,power_prices2], ["Profit","Power price, scenario 1 (high)", "Power price, scenario 2 (low)"], loc='upper center', bbox_to_anchor=(0, -0.125),fancybox=True, shadow=True, ncol=5)
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,fancybox=False, shadow=False, ncol=5,bbox_to_anchor=(0.2, 1))
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
