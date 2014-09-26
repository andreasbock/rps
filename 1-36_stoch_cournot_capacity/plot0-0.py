#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  3921035.200,    e2  7836140.800,    e3  1.174532E+7,    e4  1.564856E+7,    e5  1.954588E+7,    e6  2.343727E+7,    e7  2.732272E+7,    e8  3.120225E+7,    e9  3.507585E+7,    e10 3.894352E+7,    e11 4.280526E+7,    e12 4.666107E+7,    e13 5.051095E+7
e14 5.435490E+7,    e15 5.819292E+7,    e16 6.202501E+7,    e17 6.585117E+7,    e18 6.967140E+7,    e19 7.348571E+7,    e20 7.729408E+7,    e21 8.109652E+7,    e22 8.489304E+7,    e23 8.868362E+7,    e24 9.246828E+7,    e25 9.624700E+7,    e26 1.000198E+8
e27 1.037867E+8,    e28 1.075476E+8,    e29 1.113026E+8,    e30 1.150517E+8,    e31 1.187948E+8,    e32 1.225320E+8,    e33 1.262633E+8,    e34 1.299887E+8,    e35 1.337081E+8,    e36 1.374216E+8,    e37 1.411292E+8,    e38 1.448308E+8,    e39 1.485265E+8
e40 1.522163E+8,    e41 1.559002E+8,    e42 1.595781E+8,    e43 1.632501E+8,    e44 1.669161E+8,    e45 1.705763E+8,    e46 1.742305E+8,    e47 1.778788E+8,    e48 1.815211E+8,    e49 1.851575E+8,    e50 1.887880E+8,    e51 1.924126E+8,    e52 1.960312E+8
e53 1.996439E+8,    e54 2.032506E+8,    e55 2.068515E+8,    e56 2.104464E+8,    e57 2.140354E+8,    e58 2.176184E+8,    e59 2.211955E+8,    e60 2.247667E+8,    e61 2.283320E+8,    e62 2.318913E+8,    e63 2.354447E+8,    e64 2.389922E+8,    e65 2.425337E+8
e66 2.460693E+8,    e67 2.495990E+8,    e68 2.531228E+8,    e69 2.566406E+8,    e70 2.601525E+8,    e71 2.636584E+8,    e72 2.671585E+8,    e73 2.706526E+8,    e74 2.741408E+8,    e75 2.776230E+8,    e76 2.810993E+8,    e77 2.845697E+8,    e78 2.880342E+8
e79 2.914927E+8,    e80 2.949453E+8"""

profit_n_raw ="""e1  7.843250E+8,    e2  7.838890E+8,    e3  7.834530E+8,    e4  7.830170E+8,    e5  7.825810E+8,    e6  7.821450E+8,    e7  7.817090E+8,    e8  7.812730E+8,    e9  7.808370E+8,    e10 7.804010E+8,    e11 7.799650E+8,    e12 7.795290E+8,    e13 7.790930E+8
e14 7.786570E+8,    e15 7.782210E+8,    e16 7.777850E+8,    e17 7.773490E+8,    e18 7.769130E+8,    e19 7.764770E+8,    e20 7.760410E+8,    e21 7.756050E+8,    e22 7.751690E+8,    e23 7.747330E+8,    e24 7.742970E+8,    e25 7.738610E+8,    e26 7.734250E+8
e27 7.729890E+8,    e28 7.725530E+8,    e29 7.721170E+8,    e30 7.716810E+8,    e31 7.712450E+8,    e32 7.708090E+8,    e33 7.703730E+8,    e34 7.699370E+8,    e35 7.695010E+8,    e36 7.690650E+8,    e37 7.686290E+8,    e38 7.681930E+8,    e39 7.677570E+8
e40 7.673210E+8,    e41 7.668850E+8,    e42 7.664490E+8,    e43 7.660130E+8,    e44 7.655770E+8,    e45 7.651410E+8,    e46 7.647050E+8,    e47 7.642690E+8,    e48 7.638330E+8,    e49 7.633970E+8,    e50 7.629610E+8,    e51 7.625250E+8,    e52 7.620890E+8
e53 7.616530E+8,    e54 7.612170E+8,    e55 7.607810E+8,    e56 7.603450E+8,    e57 7.599090E+8,    e58 7.594730E+8,    e59 7.590370E+8,    e60 7.586010E+8,    e61 7.581650E+8,    e62 7.577290E+8,    e63 7.572930E+8,    e64 7.568570E+8,    e65 7.564210E+8
e66 7.559850E+8,    e67 7.555490E+8,    e68 7.551130E+8,    e69 7.546770E+8,    e70 7.542410E+8,    e71 7.538050E+8,    e72 7.533690E+8,    e73 7.529330E+8,    e74 7.524970E+8,    e75 7.520610E+8,    e76 7.516250E+8,    e77 7.511890E+8,    e78 7.507530E+8
e79 7.503170E+8,    e80 7.498810E+8"""

rec_price_raw= """"""

# THIS DETERMINES TO USE MATRIX OR THE ARRAY PROFIT
one_dim = True


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

if False:
	pass
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
