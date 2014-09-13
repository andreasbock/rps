#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  6964655.695,    e2  1.390662E+7,    e3  2.082590E+7,    e4  2.772249E+7,    e5  3.459639E+7,    e6  4.144761E+7,    e7  4.827613E+7,    e8  5.508196E+7,    e9  6.186511E+7,    e10 6.862557E+7,    e11 7.536334E+7,    e12 8.207842E+7,    e13 8.877081E+7
e14 9.544052E+7,    e15 1.020875E+8,    e16 1.087119E+8,    e17 1.153135E+8,    e18 1.218924E+8,    e19 1.284487E+8,    e20 1.349823E+8,    e21 1.414932E+8,    e22 1.479814E+8,    e23 1.544469E+8,    e24 1.608897E+8,    e25 1.673098E+8,    e26 1.737072E+8
e27 1.800820E+8,    e28 1.864341E+8,    e29 1.927634E+8,    e30 1.990701E+8,    e31 2.053541E+8,    e32 2.116154E+8,    e33 2.178541E+8,    e34 2.240700E+8,    e35 2.302632E+8,    e36 2.364338E+8,    e37 2.425816E+8,    e38 2.487068E+8,    e39 2.548093E+8
e40 2.608891E+8,    e41 2.669462E+8,    e42 2.729806E+8,    e43 2.789924E+8,    e44 2.849814E+8,    e45 2.909478E+8,    e46 2.968915E+8,    e47 3.028124E+8,    e48 3.087107E+8,    e49 3.145863E+8,    e50 3.204392E+8,    e51 3.262695E+8,    e52 3.320770E+8
e53 3.378618E+8,    e54 3.436240E+8,    e55 3.493635E+8,    e56 3.550803E+8,    e57 3.607744E+8,    e58 3.664458E+8,    e59 3.720945E+8,    e60 3.777205E+8,    e61 3.833238E+8,    e62 3.889045E+8,    e63 3.944625E+8,    e64 3.999977E+8,    e65 4.055103E+8
e66 4.110002E+8,    e67 4.164674E+8,    e68 4.219119E+8,    e69 4.273338E+8,    e70 4.327329E+8,    e71 4.381094E+8,    e72 4.434631E+8,    e73 4.487942E+8,    e74 4.541026E+8,    e75 4.593883E+8,    e76 4.646513E+8,    e77 4.698916E+8,    e78 4.751092E+8
e79 4.803042E+8,    e80 4.854764E+8"""

profit_n_raw ="""e1  6964605.467,    e2  1.390706E+7,    e3  2.082737E+7,    e4  2.772553E+7,    e5  3.460154E+7,    e6  4.145540E+7,    e7  4.828711E+7,    e8  5.509667E+7,    e9  6.188408E+7,    e10 6.864935E+7,    e11 7.539246E+7,    e12 8.211343E+7,    e13 8.881224E+7
e14 9.548891E+7,    e15 1.021434E+8,    e16 1.087758E+8,    e17 1.153860E+8,    e18 1.219741E+8,    e19 1.285400E+8,    e20 1.350838E+8,    e21 1.416054E+8,    e22 1.481049E+8,    e23 1.545822E+8,    e24 1.610374E+8,    e25 1.674704E+8,    e26 1.738813E+8
e27 1.802700E+8,    e28 1.866366E+8,    e29 1.929810E+8,    e30 1.993033E+8,    e31 2.056035E+8,    e32 2.118814E+8,    e33 2.181373E+8,    e34 2.243710E+8,    e35 2.305825E+8,    e36 2.367719E+8,    e37 2.429391E+8,    e38 2.490842E+8,    e39 2.552072E+8
e40 2.613079E+8,    e41 2.673866E+8,    e42 2.734431E+8,    e43 2.794774E+8,    e44 2.854896E+8,    e45 2.914797E+8,    e46 2.974476E+8,    e47 3.033933E+8,    e48 3.093169E+8,    e49 3.152184E+8,    e50 3.210977E+8,    e51 3.269548E+8,    e52 3.327898E+8
e53 3.386027E+8,    e54 3.443934E+8,    e55 3.501619E+8,    e56 3.559083E+8,    e57 3.616326E+8,    e58 3.673347E+8,    e59 3.730147E+8,    e60 3.786725E+8,    e61 3.843081E+8,    e62 3.899217E+8,    e63 3.955130E+8,    e64 4.010822E+8,    e65 4.066293E+8
e66 4.121542E+8,    e67 4.176570E+8,    e68 4.231376E+8,    e69 4.285961E+8,    e70 4.340324E+8,    e71 4.394466E+8,    e72 4.448386E+8,    e73 4.502085E+8,    e74 4.555562E+8,    e75 4.608818E+8,    e76 4.661852E+8,    e77 4.714665E+8,    e78 4.767256E+8
e79 4.819626E+8,    e80 4.871774E+8"""

rec_price_raw= """"""

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
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,fancybox=False, shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
