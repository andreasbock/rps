#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  1.821872E+7,    e2  3.625088E+7,    e3  5.409649E+7,    e4  7.175553E+7,    e5  8.922802E+7,    e6  1.065140E+8,    e7  1.236133E+8,    e8  1.405261E+8,    e9  1.572524E+8,    e10 1.737921E+8,    e11 1.901452E+8,    e12 2.063118E+8,    e13 2.222918E+8
e14 2.380853E+8,    e15 2.536922E+8,    e16 2.691126E+8,    e17 2.843463E+8,    e18 2.993936E+8,    e19 3.142543E+8,    e20 3.289284E+8,    e21 3.434159E+8,    e22 3.577169E+8,    e23 3.718314E+8,    e24 3.857592E+8,    e25 3.995006E+8,    e26 4.130553E+8
e27 4.264235E+8,    e28 4.396052E+8,    e29 4.526003E+8,    e30 4.654088E+8,    e31 4.780308E+8,    e32 4.904662E+8,    e33 5.027151E+8,    e34 5.147774E+8,    e35 5.266531E+8,    e36 5.383423E+8,    e37 5.498449E+8,    e38 5.611610E+8,    e39 5.722905E+8
e40 5.832335E+8,    e41 5.939899E+8,    e42 6.045597E+8,    e43 6.149430E+8,    e44 6.251397E+8,    e45 6.351499E+8,    e46 6.449735E+8,    e47 6.532932E+8,    e48 6.586795E+8,    e49 6.637111E+8,    e50 1.887880E+8,    e51 1.924126E+8,    e52 1.960312E+8
e53 1.996439E+8,    e54 2.032506E+8,    e55 2.068515E+8,    e56 2.104464E+8,    e57 2.140354E+8,    e58 2.176184E+8,    e59 2.211955E+8,    e60 2.247667E+8,    e61 2.283320E+8,    e62 2.318913E+8,    e63 2.354447E+8,    e64 2.389922E+8,    e65 2.425337E+8
e66 2.460693E+8,    e67 2.495990E+8,    e68 2.531228E+8,    e69 2.566406E+8,    e70 2.601525E+8,    e71 2.636584E+8,    e72 2.671585E+8,    e73 2.706526E+8,    e74 2.741408E+8,    e75 2.776230E+8,    e76 2.810993E+8,    e77 2.845697E+8,    e78 2.880342E+8
e79 2.914927E+8,    e80 2.949453E+8"""

profit_n_raw ="""e1  1.392829E+7,    e2  2.781075E+7,    e3  4.164739E+7,    e4  5.543821E+7,    e5  6.918320E+7,    e6  8.288237E+7,    e7  9.653572E+7,    e8  1.101432E+8,    e9  1.237049E+8,    e10 1.372208E+8,    e11 1.506909E+8,    e12 1.641151E+8,    e13 1.774935E+8
e14 1.908261E+8,    e15 2.041128E+8,    e16 2.173538E+8,    e17 2.305489E+8,    e18 2.436982E+8,    e19 2.568016E+8,    e20 2.698593E+8,    e21 2.828711E+8,    e22 2.958371E+8,    e23 3.087572E+8,    e24 3.216316E+8,    e25 3.344601E+8,    e26 3.472428E+8
e27 3.599797E+8,    e28 3.726707E+8,    e29 3.853159E+8,    e30 3.979153E+8,    e31 4.104689E+8,    e32 4.229767E+8,    e33 4.354386E+8,    e34 4.478547E+8,    e35 4.602250E+8,    e36 4.725495E+8,    e37 4.848281E+8,    e38 4.970609E+8,    e39 5.092479E+8
e40 5.213891E+8,    e41 5.334844E+8,    e42 5.455339E+8,    e43 5.575376E+8,    e44 5.694955E+8,    e45 5.814075E+8,    e46 5.932737E+8,    e47 6.053929E+8,    e48 6.180361E+8,    e49 6.305922E+8,    e50 7.629610E+8,    e51 7.625250E+8,    e52 7.620890E+8
e53 7.616530E+8,    e54 7.612170E+8,    e55 7.607810E+8,    e56 7.603450E+8,    e57 7.599090E+8,    e58 7.594730E+8,    e59 7.590370E+8,    e60 7.586010E+8,    e61 7.581650E+8,    e62 7.577290E+8,    e63 7.572930E+8,    e64 7.568570E+8,    e65 7.564210E+8
e66 7.559850E+8,    e67 7.555490E+8,    e68 7.551130E+8,    e69 7.546770E+8,    e70 7.542410E+8,    e71 7.538050E+8,    e72 7.533690E+8,    e73 7.529330E+8,    e74 7.524970E+8,    e75 7.520610E+8,    e76 7.516250E+8,    e77 7.511890E+8,    e78 7.507530E+8
e79 7.503170E+8,    e80 7.498810E+8"""

rec_price_raw= """e1  397.650,    e2  395.300,    e3  392.950,    e4  390.600,    e5  388.250,    e6  385.900,    e7  383.550,    e8  381.200,    e9  378.850,    e10 376.500,    e11 374.150,    e12 371.800,    e13 369.450,    e14 367.100,    e15 364.750,    e16 362.400
e17 360.050,    e18 357.700,    e19 355.350,    e20 353.000,    e21 350.650,    e22 348.300,    e23 345.950,    e24 343.600,    e25 341.250,    e26 338.900,    e27 336.550,    e28 334.200,    e29 331.850,    e30 329.500,    e31 327.150,    e32 324.800
e33 322.450,    e34 320.100,    e35 317.750,    e36 315.400,    e37 313.050,    e38 310.700,    e39 308.350,    e40 306.000,    e41 303.650,    e42 301.300,    e43 298.950,    e44 296.600,    e45 294.250,    e46 291.900,    e47 288.800,    e48 284.200
e49 279.600"""

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
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,fancybox=False,bbox_to_anchor=(0.2, 1.05),shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
