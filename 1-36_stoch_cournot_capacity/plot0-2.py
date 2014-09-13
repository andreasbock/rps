#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  2.906128E+7,    e2  5.764670E+7,    e3  8.575628E+7,    e4  1.133900E+8,    e5  1.405479E+8,    e6  1.672299E+8,    e7  1.934361E+8,    e8  2.191664E+8,    e9  2.444209E+8,    e10 2.691995E+8,    e11 2.935023E+8,    e12 3.173292E+8,    e13 3.406803E+8
e14 3.635555E+8,    e15 3.859549E+8,    e16 1.045172E+8,    e17 1.109487E+8,    e18 1.173684E+8,    e19 1.237762E+8,    e20 1.301722E+8,    e21 1.365562E+8,    e22 1.429285E+8,    e23 1.492888E+8,    e24 1.556374E+8,    e25 1.619740E+8,    e26 1.682988E+8
e27 1.746117E+8,    e28 1.809128E+8,    e29 1.872020E+8,    e30 1.934794E+8,    e31 1.997449E+8,    e32 2.059985E+8,    e33 2.122403E+8,    e34 2.184702E+8,    e35 2.246882E+8,    e36 2.308944E+8,    e37 2.370888E+8,    e38 2.432713E+8,    e39 2.494419E+8
e40 2.556006E+8,    e41 2.617475E+8,    e42 2.678826E+8,    e43 2.740058E+8,    e44 2.801171E+8,    e45 2.862166E+8,    e46 2.923042E+8,    e47 2.983799E+8,    e48 3.044438E+8,    e49 3.104958E+8,    e50 3.165360E+8,    e51 3.225643E+8,    e52 3.285808E+8
e53 3.345854E+8,    e54 3.405781E+8,    e55 3.465590E+8,    e56 3.525280E+8,    e57 3.584851E+8,    e58 3.644304E+8,    e59 3.703639E+8,    e60 3.762854E+8,    e61 3.821952E+8,    e62 3.880930E+8,    e63 3.939790E+8,    e64 3.998532E+8,    e65 4.057154E+8
e66 4.115659E+8,    e67 4.174044E+8,    e68 4.232311E+8,    e69 4.290460E+8,    e70 4.348490E+8,    e71 4.406401E+8,    e72 4.464194E+8,    e73 4.521868E+8,    e74 4.579423E+8,    e75 4.636860E+8,    e76 4.694178E+8,    e77 4.751378E+8,    e78 4.808459E+8
e79 4.865422E+8,    e80 4.922266E+8"""

profit_n_raw ="""e1  2.226285E+7,    e2  4.440757E+7,    e3  6.643414E+7,    e4  8.834258E+7,    e5  1.101329E+8,    e6  1.318051E+8,    e7  1.533591E+8,    e8  1.747950E+8,    e9  1.961127E+8,    e10 2.173124E+8,    e11 2.383938E+8,    e12 2.593572E+8,    e13 2.802024E+8
e14 3.009295E+8,    e15 3.215384E+8,    e16 4.085994E+8,    e17 4.082506E+8,    e18 4.079018E+8,    e19 4.075530E+8,    e20 4.072042E+8,    e21 4.068554E+8,    e22 4.065066E+8,    e23 4.061578E+8,    e24 4.058090E+8,    e25 4.054602E+8,    e26 4.051114E+8
e27 4.047626E+8,    e28 4.044138E+8,    e29 4.040650E+8,    e30 4.037162E+8,    e31 4.033674E+8,    e32 4.030186E+8,    e33 4.026698E+8,    e34 4.023210E+8,    e35 4.019722E+8,    e36 4.016234E+8,    e37 4.012746E+8,    e38 4.009258E+8,    e39 4.005770E+8
e40 4.002282E+8,    e41 3.998794E+8,    e42 3.995307E+8,    e43 3.991818E+8,    e44 3.988331E+8,    e45 3.984843E+8,    e46 3.981354E+8,    e47 3.977866E+8,    e48 3.974378E+8,    e49 3.970891E+8,    e50 3.967403E+8,    e51 3.963914E+8,    e52 3.960426E+8
e53 3.956938E+8,    e54 3.953450E+8,    e55 3.949963E+8,    e56 3.946474E+8,    e57 3.942986E+8,    e58 3.939499E+8,    e59 3.936010E+8,    e60 3.932523E+8,    e61 3.929034E+8,    e62 3.925546E+8,    e63 3.922058E+8,    e64 3.918571E+8,    e65 3.915082E+8
e66 3.911594E+8,    e67 3.908106E+8,    e68 3.904618E+8,    e69 3.901131E+8,    e70 3.897643E+8,    e71 3.894154E+8,    e72 3.890666E+8,    e73 3.887178E+8,    e74 3.883690E+8,    e75 3.880203E+8,    e76 3.876714E+8,    e77 3.873226E+8,    e78 3.869738E+8
e79 3.866250E+8,    e80 3.862763E+8"""

rec_price_raw= """e1  396.240,    e2  392.480,    e3  388.720,    e4  384.960,    e5  381.200,    e6  377.440,    e7  373.680,    e8  369.920,    e9  366.160,    e10 362.400,    e11 358.640,    e12 354.880,    e13 351.120,    e14 347.360,    e15 343.600"""

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
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,fancybox=False,bbox_to_anchor=(0.2, 1),shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
