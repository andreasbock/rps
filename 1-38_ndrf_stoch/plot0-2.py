#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  4348688.914,    e2  8674755.657,    e3  1.297820E+7,    e4  1.725902E+7,    e5  2.151722E+7,    e6  2.575280E+7,    e7  2.996576E+7,    e8  3.415609E+7,    e9  3.832380E+7,    e10 4.246889E+7,    e11 4.659136E+7,    e12 5.069120E+7,    e13 5.476843E+7
e14 5.882303E+7,    e15 6.285501E+7,    e16 6.686436E+7,    e17 7.085110E+7,    e18 7.481521E+7,    e19 7.875670E+7,    e20 8.267557E+7,    e21 8.657181E+7,    e22 9.044543E+7,    e23 9.429644E+7,    e24 9.812481E+7,    e25 1.019306E+8,    e26 1.057137E+8
e27 1.094742E+8,    e28 1.132121E+8,    e29 1.169274E+8,    e30 1.206200E+8,    e31 1.242900E+8,    e32 1.279374E+8,    e33 1.315622E+8,    e34 1.351644E+8,    e35 1.387439E+8,    e36 1.423008E+8,    e37 1.458351E+8,    e38 1.493468E+8,    e39 1.528358E+8
e40 1.563023E+8,    e41 1.597461E+8,    e42 1.631672E+8,    e43 1.665658E+8,    e44 1.699417E+8,    e45 1.732951E+8,    e46 1.766257E+8,    e47 1.798460E+8,    e48 1.828605E+8,    e49 1.858412E+8,    e50 1.887880E+8,    e51 1.885731E+8,    e52 1.886279E+8
e53 1.885455E+8,    e54 1.884615E+8,    e55 1.883760E+8,    e56 1.882889E+8,    e57 1.882002E+8,    e58 1.881099E+8,    e59 1.880181E+8,    e60 1.879247E+8,    e61 1.878298E+8,    e62 1.877332E+8,    e63 1.876351E+8,    e64 1.875355E+8,    e65 1.874342E+8
e66 1.873314E+8,    e67 1.872270E+8,    e68 1.871211E+8,    e69 1.870136E+8,    e70 1.869045E+8,    e71 1.869774E+8,    e72 1.870496E+8,    e73 1.871211E+8,    e74 1.871919E+8,    e75 1.872620E+8,    e76 1.873314E+8,    e77 1.874001E+8,    e78 1.874681E+8
e79 1.875355E+8,    e80 1.876021E+8"""

profit_n_raw ="""e1  1.739580E+7,    e2  3.470478E+7,    e3  5.192697E+7,    e4  6.906234E+7,    e5  8.611090E+7,    e6  1.030727E+8,    e7  1.199476E+8,    e8  1.367358E+8,    e9  1.534371E+8,    e10 1.700516E+8,    e11 1.865793E+8,    e12 2.030202E+8,    e13 2.193744E+8
e14 2.356416E+8,    e15 2.518221E+8,    e16 2.679158E+8,    e17 2.839227E+8,    e18 2.998428E+8,    e19 3.156760E+8,    e20 3.314225E+8,    e21 3.470821E+8,    e22 3.626549E+8,    e23 3.781410E+8,    e24 3.935402E+8,    e25 4.088526E+8,    e26 4.240782E+8
e27 4.392170E+8,    e28 4.542690E+8,    e29 4.692342E+8,    e30 4.841125E+8,    e31 4.989041E+8,    e32 5.136089E+8,    e33 5.282268E+8,    e34 5.427580E+8,    e35 5.572023E+8,    e36 5.715598E+8,    e37 5.858305E+8,    e38 6.000145E+8,    e39 6.141116E+8
e40 6.281219E+8,    e41 6.420453E+8,    e42 6.558820E+8,    e43 6.696319E+8,    e44 6.832950E+8,    e45 6.968712E+8,    e46 7.103607E+8,    e47 7.237547E+8,    e48 7.369909E+8,    e49 7.500596E+8,    e50 7.629610E+8,    e51 7.629610E+8,    e52 7.629610E+8
e53 7.629610E+8,    e54 7.629610E+8,    e55 7.629610E+8,    e56 7.629610E+8,    e57 7.629610E+8,    e58 7.629610E+8,    e59 7.629610E+8,    e60 7.629610E+8,    e61 7.629610E+8,    e62 7.629610E+8,    e63 7.629610E+8,    e64 7.629610E+8,    e65 7.629610E+8
e66 7.629610E+8,    e67 7.629610E+8,    e68 7.629610E+8,    e69 7.629610E+8,    e70 7.629610E+8,    e71 7.629610E+8,    e72 7.629610E+8,    e73 7.629610E+8,    e74 7.629610E+8,    e75 7.629610E+8,    e76 7.629610E+8,    e77 7.629610E+8,    e78 7.629610E+8
e79 7.629610E+8,    e80 7.629610E+8"""

rec_price_raw= """"""

rc('text',usetex=True)
rc('font',family='serif')
profit_raw_split = profit_raw.split('\n')
rows = len(profit_raw_split)

profit_n = np.zeros(shape=(80))
i = 0
for p_raw in profit_n_raw.split('\n'):
	for p_raw2 in p_raw.split(','):
		profit_n[i] = float(p_raw2.split()[1])
		i+=1
profit_r = np.zeros(shape=(80))
i = 0
for p_raw in profit_r_raw.split('\n'):
	for p_raw2 in p_raw.split(','):
		profit_r[i] = float(p_raw2.split()[1])
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
	ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='lower right',frameon=False,fancybox=False, shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
	fig.savefig("foo.svg",bbox_inches='tight')
