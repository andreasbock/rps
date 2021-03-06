#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  3307917.714,    e2  6581796.571,    e3  9821636.571,    e4  1.302744E+7,    e5  1.619920E+7,    e6  1.933692E+7,    e7  2.244061E+7,    e8  2.551025E+7,    e9  2.854586E+7,    e10 3.154743E+7,    e11 3.451496E+7,    e12 3.744845E+7,    e13 4.034790E+7
e14 4.321331E+7,    e15 3.018658E+7,    e16 2.769788E+7,    e17 2.913967E+7,    e18 3.054742E+7,    e19 3.192113E+7,    e20 3.326080E+7,    e21 3.456643E+7,    e22 3.583803E+7,    e23 3.707558E+7,    e24 3.827909E+7,    e25 3.944857E+7,    e26 4.058401E+7
e27 4.168541E+7,    e28 4.275277E+7,    e29 4.378609E+7,    e30 4.478537E+7,    e31 4.575061E+7,    e32 4.668182E+7,    e33 4.757899E+7,    e34 4.844211E+7,    e35 4.927120E+7,    e36 5.006625E+7,    e37 5.082726E+7,    e38 5.155423E+7,    e39 5.224716E+7
e40 5.290606E+7,    e41 5.353091E+7,    e42 5.412173E+7,    e43 5.467851E+7,    e44 5.520124E+7,    e45 5.568994E+7,    e46 5.614460E+7,    e47 5.656523E+7,    e48 5.695181E+7,    e49 5.730435E+7,    e50 5.762286E+7,    e51 5.790732E+7,    e52 5.815775E+7
e53 5.837414E+7,    e54 5.855649E+7,    e55 5.870480E+7,    e56 5.881907E+7,    e57 5.889931E+7,    e58 5.894550E+7,    e59 5.895765E+7,    e60 5.893577E+7,    e61 5.887985E+7,    e62 5.878989E+7,    e63 5.866589E+7,    e64 5.850785E+7,    e65 5.831577E+7
e66 5.808965E+7,    e67 5.782950E+7,    e68 5.753531E+7,    e69 5.720707E+7,    e70 5.684480E+7,    e71 5.644849E+7,    e72 5.601814E+7,    e73 5.555375E+7,    e74 5.505532E+7,    e75 5.452286E+7,    e76 5.395635E+7,    e77 5.335581E+7,    e78 5.272123E+7
e79 5.205260E+7,    e80 5.134994E+7"""

profit_n_raw ="""e1  1.951965E+8,    e2  1.920579E+8,    e3  1.889436E+8,    e4  1.858536E+8,    e5  1.827880E+8,    e6  1.797466E+8,    e7  1.767296E+8,    e8  1.737369E+8,    e9  1.707685E+8,    e10 1.678245E+8,    e11 1.649047E+8,    e12 1.620093E+8,    e13 1.591382E+8
e14 1.562914E+8,    e15 1.649791E+8,    e16 1.650013E+8,    e17 1.621130E+8,    e18 1.592490E+8,    e19 1.564094E+8,    e20 1.535940E+8,    e21 1.508030E+8,    e22 1.480363E+8,    e23 1.452939E+8,    e24 1.425758E+8,    e25 1.398821E+8,    e26 1.372127E+8
e27 1.345675E+8,    e28 1.319467E+8,    e29 1.293502E+8,    e30 1.267781E+8,    e31 1.242302E+8,    e32 1.217067E+8,    e33 1.192074E+8,    e34 1.167325E+8,    e35 1.142819E+8,    e36 1.118557E+8,    e37 1.094537E+8,    e38 1.070761E+8,    e39 1.047227E+8
e40 1.023937E+8,    e41 1.000890E+8,    e42 9.780866E+7,    e43 9.555260E+7,    e44 9.332085E+7,    e45 9.111342E+7,    e46 8.893031E+7,    e47 8.677151E+7,    e48 8.463703E+7,    e49 8.252687E+7,    e50 8.044102E+7,    e51 7.837949E+7,    e52 7.634227E+7
e53 7.432937E+7,    e54 7.234079E+7,    e55 7.037652E+7,    e56 6.843657E+7,    e57 6.652094E+7,    e58 6.462962E+7,    e59 6.276262E+7,    e60 6.091993E+7,    e61 5.910157E+7,    e62 5.730751E+7,    e63 5.553778E+7,    e64 5.379236E+7,    e65 5.207125E+7
e66 5.037446E+7,    e67 4.870199E+7,    e68 4.705384E+7,    e69 4.543000E+7,    e70 4.383047E+7,    e71 4.225527E+7,    e72 4.070438E+7,    e73 3.917780E+7,    e74 3.767554E+7,    e75 3.619760E+7,    e76 3.474398E+7,    e77 3.331467E+7,    e78 3.190967E+7
e79 3.052900E+7,    e80 2.917264E+7"""

rec_price_raw= """e1  50.000,    e2  50.000,    e3  50.000,    e4  50.000,    e5  50.000,    e6  50.000,    e7  50.000,    e8  50.000,    e9  50.000,    e10 50.000,    e11 50.000,    e12 50.000,    e13 50.000,    e14 30.400,    e15  4.000"""

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
