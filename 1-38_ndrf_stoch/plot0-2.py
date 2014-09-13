#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  6947913.295,    e2  1.383965E+7,    e3  2.067522E+7,    e4  2.745461E+7,    e5  3.417783E+7,    e6  4.084488E+7,    e7  4.745575E+7,    e8  5.401045E+7,    e9  6.050898E+7,    e10 6.695133E+7,    e11 7.333751E+7,    e12 7.966751E+7,    e13 8.594135E+7
e14 9.215901E+7,    e15 9.832049E+7,    e16 1.044258E+8,    e17 1.104749E+8,    e18 1.164679E+8,    e19 1.224047E+8,    e20 1.282853E+8,    e21 1.341098E+8,    e22 1.398780E+8,    e23 1.455901E+8,    e24 1.512461E+8,    e25 1.568458E+8,    e26 1.623894E+8
e27 1.678768E+8,    e28 1.733080E+8,    e29 1.786831E+8,    e30 1.840020E+8,    e31 1.891483E+8,    e32 1.903928E+8,    e33 1.903702E+8,    e34 1.903468E+8,    e35 1.903227E+8,    e36 1.902980E+8,    e37 1.902725E+8,    e38 1.902463E+8,    e39 1.902195E+8
e40 1.901919E+8,    e41 1.901637E+8,    e42 1.901347E+8,    e43 1.901051E+8,    e44 1.900747E+8,    e45 1.901637E+8,    e46 1.902463E+8,    e47 1.903227E+8,    e48 1.903928E+8,    e49 1.904567E+8,    e50 1.905142E+8,    e51 1.905655E+8,    e52 1.906105E+8
e53 1.906492E+8,    e54 1.906816E+8,    e55 1.907078E+8,    e56 1.907277E+8,    e57 1.907413E+8,    e58 1.907486E+8,    e59 1.907497E+8,    e60 1.907444E+8,    e61 1.907329E+8,    e62 1.907151E+8,    e63 1.906911E+8,    e64 1.906607E+8,    e65 1.906241E+8
e66 1.905812E+8,    e67 1.905320E+8,    e68 1.904765E+8,    e69 1.904148E+8,    e70 1.903468E+8,    e71 1.902725E+8,    e72 1.901919E+8,    e73 1.901051E+8,    e74 1.900119E+8,    e75 1.899125E+8,    e76 1.898068E+8,    e77 1.896949E+8,    e78 1.895766E+8
e79 1.894521E+8,    e80 1.893213E+8"""

profit_n_raw ="""e1  2.779119E+7,    e2  5.535933E+7,    e3  8.270441E+7,    e4  1.098264E+8,    e5  1.367254E+8,    e6  1.634013E+8,    e7  1.898542E+8,    e8  2.160840E+8,    e9  2.420907E+8,    e10 2.678744E+8,    e11 2.934350E+8,    e12 3.187726E+8,    e13 3.438871E+8
e14 3.687786E+8,    e15 3.934470E+8,    e16 4.178924E+8,    e17 4.421147E+8,    e18 4.661139E+8,    e19 4.898901E+8,    e20 5.134432E+8,    e21 5.367733E+8,    e22 5.598803E+8,    e23 5.827643E+8,    e24 6.054252E+8,    e25 6.278630E+8,    e26 6.500778E+8
e27 6.720695E+8,    e28 6.938382E+8,    e29 7.153839E+8,    e30 7.367064E+8,    e31 7.577600E+8,    e32 7.629610E+8,    e33 7.629610E+8,    e34 7.629610E+8,    e35 7.629610E+8,    e36 7.629610E+8,    e37 7.629610E+8,    e38 7.629610E+8,    e39 7.629610E+8
e40 7.629610E+8,    e41 7.629610E+8,    e42 7.629610E+8,    e43 7.629610E+8,    e44 7.629610E+8,    e45 7.629610E+8,    e46 7.629610E+8,    e47 7.629610E+8,    e48 7.629610E+8,    e49 7.629610E+8,    e50 7.629610E+8,    e51 7.629610E+8,    e52 7.629610E+8
e53 7.629610E+8,    e54 7.629610E+8,    e55 7.629610E+8,    e56 7.629610E+8,    e57 7.629610E+8,    e58 7.629610E+8,    e59 7.629610E+8,    e60 7.629610E+8,    e61 7.629610E+8,    e62 7.629610E+8,    e63 7.629610E+8,    e64 7.629610E+8,    e65 7.629610E+8
e66 7.629610E+8,    e67 7.629610E+8,    e68 7.629610E+8,    e69 7.629610E+8,    e70 7.629610E+8,    e71 7.629610E+8,    e72 7.629610E+8,    e73 7.629610E+8,    e74 7.629610E+8,    e75 7.629610E+8,    e76 7.629610E+8,    e77 7.629610E+8,    e78 7.629610E+8
e79 7.629610E+8,    e80 7.629610E+8"""

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
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='lower right',frameon=False,fancybox=False, shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
