#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """"""

profit_n_raw ="""e1  7.847610E+8,    e2  7.847610E+8,    e3  7.847610E+8,    e4  7.847610E+8,    e5  7.847610E+8,    e6  7.847610E+8,    e7  7.847610E+8,    e8  7.847610E+8,    e9  7.847610E+8,    e10 7.847610E+8,    e11 7.847610E+8,    e12 7.847610E+8,    e13 7.847610E+8
e14 7.847610E+8,    e15 7.847610E+8,    e16 7.847610E+8,    e17 7.847610E+8,    e18 7.847610E+8,    e19 7.847610E+8,    e20 7.847610E+8,    e21 7.847610E+8,    e22 7.847610E+8,    e23 7.847610E+8,    e24 7.847610E+8,    e25 7.847610E+8,    e26 7.847610E+8
e27 7.847610E+8,    e28 7.847610E+8,    e29 7.847610E+8,    e30 7.847610E+8,    e31 7.847610E+8,    e32 7.847610E+8,    e33 7.847610E+8,    e34 7.847610E+8,    e35 7.847610E+8,    e36 7.847610E+8,    e37 7.847610E+8,    e38 7.847610E+8,    e39 7.847610E+8
e40 7.847610E+8,    e41 7.847610E+8,    e42 7.847610E+8,    e43 7.847610E+8,    e44 7.847610E+8,    e45 7.847610E+8,    e46 7.847610E+8,    e47 7.847610E+8,    e48 7.847610E+8,    e49 7.847610E+8,    e50 7.847610E+8,    e51 7.847610E+8,    e52 7.847610E+8
e53 7.847610E+8,    e54 7.847610E+8,    e55 7.847610E+8,    e56 7.847610E+8,    e57 7.847610E+8,    e58 7.847610E+8,    e59 7.847610E+8,    e60 7.847610E+8,    e61 7.847610E+8,    e62 7.847610E+8,    e63 7.847610E+8,    e64 7.847610E+8,    e65 7.847610E+8
e66 7.847610E+8,    e67 7.847610E+8,    e68 7.847610E+8,    e69 7.847610E+8,    e70 7.847610E+8,    e71 7.847610E+8,    e72 7.847610E+8,    e73 7.847610E+8,    e74 7.847610E+8,    e75 7.847610E+8,    e76 7.847610E+8,    e77 7.847610E+8,    e78 7.847610E+8
e79 7.847610E+8,    e80 7.847610E+8"""

rec_price_raw= """"""

rc('text',usetex=True)
rc('font',family='serif')
profit_raw_split = profit_raw.split('\n')
rows = len(profit_raw_split)

profit_r = np.zeros(shape=(80))
profit_n = np.zeros(shape=(80))
i = 0
for p_raw in profit_n_raw.split('\n'):
	for p_raw2 in p_raw.split(','):
		profit_n[i] = float(p_raw2.split()[1])
		i+=1

rec_price = np.zeros(shape=(80))

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

	rc('text.latex', unicode=True) 
	ax2.set_ylabel(u"REC Price (\u20AC)")
	rec_price_plot, = ax2.plot(x,rec_price,'-',linewidth=2,c='black')
	ax.set_xlabel(r"Renewable Capacity (MW)")
	ax.set_ylabel(u"Profit of the producers (\u20AC)")
	profit_r_plt,= ax.plot(x,profit_r,'--',linewidth=4, c='black')
	profit_n_plt,= ax.plot(x,profit_n,'-.',linewidth=2, c='black')
	ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,fancybox=False, shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
	fig.savefig("foo.svg",bbox_inches='tight')
