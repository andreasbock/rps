#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1 4315370.210"""

profit_n_raw ="""e1  2.052833E+9,    e2  2.056279E+9,    e3  2.056279E+9,    e4  2.056279E+9,    e5  2.056279E+9,    e6  2.056279E+9,    e7  2.056279E+9,    e8  2.056279E+9,    e9  2.056279E+9,    e10 2.056279E+9,    e11 2.056279E+9,    e12 2.056279E+9,    e13 2.056279E+9
e14 2.056279E+9,    e15 2.056279E+9,    e16 2.056279E+9,    e17 2.056279E+9,    e18 2.056279E+9,    e19 2.056279E+9,    e20 2.056279E+9,    e21 2.056279E+9,    e22 2.056279E+9,    e23 2.056279E+9,    e24 2.056279E+9,    e25 2.056279E+9,    e26 2.056279E+9
e27 2.056279E+9,    e28 2.056279E+9,    e29 2.056279E+9,    e30 2.056279E+9,    e31 2.056279E+9,    e32 2.056279E+9,    e33 2.056279E+9,    e34 2.056279E+9,    e35 2.056279E+9,    e36 2.056279E+9,    e37 2.056279E+9,    e38 2.056279E+9,    e39 2.056279E+9
e40 2.056279E+9,    e41 2.056279E+9,    e42 2.056279E+9,    e43 2.056279E+9,    e44 2.056279E+9,    e45 2.056279E+9,    e46 2.056279E+9,    e47 2.056279E+9,    e48 2.056279E+9,    e49 2.056279E+9,    e50 2.056279E+9,    e51 2.056279E+9,    e52 2.056279E+9
e53 2.056279E+9,    e54 2.056279E+9,    e55 2.056279E+9,    e56 2.056279E+9,    e57 2.056279E+9,    e58 2.056279E+9,    e59 2.056279E+9,    e60 2.056279E+9,    e61 2.056279E+9,    e62 2.056279E+9,    e63 2.056279E+9,    e64 2.056279E+9,    e65 2.056279E+9
e66 2.056279E+9,    e67 2.056279E+9,    e68 2.056279E+9,    e69 2.056279E+9,    e70 2.056279E+9,    e71 2.056279E+9,    e72 2.056279E+9,    e73 2.056279E+9,    e74 2.056279E+9,    e75 2.056279E+9,    e76 2.056279E+9,    e77 2.056279E+9,    e78 2.056279E+9
e79 2.056279E+9,    e80 2.056279E+9"""

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
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,fancybox=False, shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
