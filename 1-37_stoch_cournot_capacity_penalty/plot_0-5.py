#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  3187780.571,    e2  6341522.286,    e3  9461225.143,    e4  1.254689E+7,    e5  1.559851E+7,    e6  1.861610E+7,    e7  2.159965E+7,    e8  2.454916E+7,    e9  2.746463E+7,    e10 3.034606E+7,    e11 3.319345E+7,    e12 3.600680E+7,    e13 3.878612E+7
e14 4.153139E+7,    e15 4.424263E+7,    e16 4.691983E+7,    e17 4.956299E+7,    e18 5.217211E+7,    e19 5.474719E+7,    e20 5.728823E+7,    e21 5.979523E+7,    e22 6.226820E+7,    e23 6.470712E+7,    e24 6.711201E+7,    e25 6.948286E+7,    e26 7.181967E+7
e27 7.412244E+7,    e28 7.639117E+7,    e29 7.862586E+7,    e30 8.082651E+7,    e31 8.299313E+7,    e32 8.512571E+7,    e33 8.722424E+7,    e34 8.928874E+7,    e35 9.131920E+7,    e36 9.331562E+7,    e37 9.065513E+7,    e38 8.369332E+7,    e39 7.623615E+7
e40 6.828361E+7,    e41 5.983571E+7,    e42 5.412173E+7,    e43 5.467851E+7,    e44 5.520124E+7,    e45 5.568994E+7,    e46 5.614460E+7,    e47 5.656523E+7,    e48 5.695181E+7,    e49 5.730435E+7,    e50 5.762286E+7,    e51 5.790732E+7,    e52 5.815775E+7
e53 5.837414E+7,    e54 5.855649E+7,    e55 5.870480E+7,    e56 5.881907E+7,    e57 5.889931E+7,    e58 5.894550E+7,    e59 5.895765E+7,    e60 5.893577E+7,    e61 5.887985E+7,    e62 5.878989E+7,    e63 5.866589E+7,    e64 5.850785E+7,    e65 5.831577E+7
e66 5.808965E+7,    e67 5.782950E+7,    e68 5.753531E+7,    e69 5.720707E+7,    e70 5.684480E+7,    e71 5.644849E+7,    e72 5.601814E+7,    e73 5.555375E+7,    e74 5.505532E+7,    e75 5.452286E+7,    e76 5.395635E+7,    e77 5.335581E+7,    e78 5.272123E+7
e79 5.205260E+7,    e80 5.134994E+7"""

profit_n_raw ="""e1  1.721987E+8,    e2  1.692318E+8,    e3  1.662891E+8,    e4  1.633708E+8,    e5  1.604768E+8,    e6  1.576071E+8,    e7  1.547617E+8,    e8  1.519407E+8,    e9  1.491440E+8,    e10 1.463715E+8,    e11 1.436234E+8,    e12 1.408996E+8,    e13 1.382002E+8
e14 1.355250E+8,    e15 1.328741E+8,    e16 1.302476E+8,    e17 1.276454E+8,    e18 1.250675E+8,    e19 1.225139E+8,    e20 1.199847E+8,    e21 1.174797E+8,    e22 1.149991E+8,    e23 1.125428E+8,    e24 1.101108E+8,    e25 1.077031E+8,    e26 1.053197E+8
e27 1.029607E+8,    e28 1.006260E+8,    e29 9.831555E+7,    e30 9.602945E+7,    e31 9.376767E+7,    e32 9.153020E+7,    e33 8.931705E+7,    e34 8.712822E+7,    e35 8.496370E+7,    e36 8.282350E+7,    e37 8.353060E+7,    e38 8.666763E+7,    e39 8.985095E+7
e40 9.308055E+7,    e41 9.635644E+7,    e42 9.780866E+7,    e43 9.555260E+7,    e44 9.332085E+7,    e45 9.111342E+7,    e46 8.893031E+7,    e47 8.677151E+7,    e48 8.463703E+7,    e49 8.252687E+7,    e50 8.044102E+7,    e51 7.837949E+7,    e52 7.634227E+7
e53 7.432937E+7,    e54 7.234079E+7,    e55 7.037652E+7,    e56 6.843657E+7,    e57 6.652094E+7,    e58 6.462962E+7,    e59 6.276262E+7,    e60 6.091993E+7,    e61 5.910157E+7,    e62 5.730751E+7,    e63 5.553778E+7,    e64 5.379236E+7,    e65 5.207125E+7
e66 5.037446E+7,    e67 4.870199E+7,    e68 4.705384E+7,    e69 4.543000E+7,    e70 4.383047E+7,    e71 4.225527E+7,    e72 4.070438E+7,    e73 3.917780E+7,    e74 3.767554E+7,    e75 3.619760E+7,    e76 3.474398E+7,    e77 3.331467E+7,    e78 3.190967E+7
e79 3.052900E+7,    e80 2.917264E+7"""

rec_price_raw= """e1  20.000,    e2  20.000,    e3  20.000,    e4  20.000,    e5  20.000,    e6  20.000,    e7  20.000,    e8  20.000,    e9  20.000,    e10 20.000,    e11 20.000,    e12 20.000,    e13 20.000,    e14 20.000,    e15 20.000,    e16 20.000,    e17 20.000
e18 20.000,    e19 20.000,    e20 20.000,    e21 20.000,    e22 20.000,    e23 20.000,    e24 20.000,    e25 20.000,    e26 20.000,    e27 20.000,    e28 20.000,    e29 20.000,    e30 20.000,    e31 20.000,    e32 20.000,    e33 20.000,    e34 20.000
e35 20.000,    e36 20.000,    e37 17.920,    e38 14.080,    e39 10.240,    e40  6.400,    e41  2.560"""

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
