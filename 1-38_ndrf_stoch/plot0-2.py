#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  6947913.295,    e2  1.383965E+7,    e3  2.067522E+7,    e4  2.745461E+7,    e5  3.417783E+7,    e6  4.084488E+7,    e7  4.745575E+7,    e8  5.401045E+7,    e9  6.050898E+7,    e10 6.695133E+7,    e11 7.333751E+7,    e12 7.966751E+7,    e13 8.594135E+7
e14 9.215901E+7,    e15 9.832049E+7,    e16 1.044258E+8,    e17 1.104749E+8,    e18 1.164679E+8,    e19 1.224047E+8,    e20 1.282853E+8,    e21 1.341098E+8,    e22 1.398780E+8,    e23 1.455901E+8,    e24 1.512461E+8,    e25 1.568458E+8,    e26 1.623894E+8
e27 1.678768E+8,    e28 1.733080E+8,    e29 1.786831E+8,    e30 1.840020E+8,    e31 1.892647E+8,    e32 1.944712E+8,    e33 1.996216E+8,    e34 2.047158E+8,    e35 2.097538E+8,    e36 2.147356E+8,    e37 2.196613E+8,    e38 2.245308E+8,    e39 2.293441E+8
e40 2.341013E+8,    e41 2.388022E+8,    e42 2.434471E+8,    e43 2.480357E+8,    e44 2.525681E+8,    e45 2.570444E+8,    e46 2.614645E+8,    e47 2.658285E+8,    e48 2.701362E+8,    e49 2.743878E+8,    e50 2.785832E+8,    e51 2.827225E+8,    e52 2.868056E+8
e53 2.908324E+8,    e54 2.948032E+8,    e55 2.987177E+8,    e56 3.025761E+8,    e57 3.063783E+8,    e58 3.101243E+8,    e59 3.138142E+8,    e60 3.174479E+8,    e61 3.210254E+8,    e62 3.245467E+8,    e63 3.280119E+8,    e64 3.314209E+8,    e65 3.347737E+8
e66 3.380703E+8,    e67 3.413108E+8,    e68 3.444951E+8,    e69 3.476232E+8,    e70 3.506951E+8,    e71 3.537109E+8,    e72 3.566705E+8,    e73 3.595740E+8,    e74 3.624212E+8,    e75 3.652123E+8,    e76 3.679472E+8,    e77 3.706259E+8,    e78 3.732485E+8
e79 3.758149E+8,    e80 3.783251E+8"""

profit_n_raw ="""e1  2.779119E+7,    e2  5.535933E+7,    e3  8.270441E+7,    e4  1.098264E+8,    e5  1.367254E+8,    e6  1.634013E+8,    e7  1.898542E+8,    e8  2.160840E+8,    e9  2.420907E+8,    e10 2.678744E+8,    e11 2.934350E+8,    e12 3.187726E+8,    e13 3.438871E+8
e14 3.687786E+8,    e15 3.934470E+8,    e16 4.178924E+8,    e17 4.421147E+8,    e18 4.661139E+8,    e19 4.898901E+8,    e20 5.134432E+8,    e21 5.367733E+8,    e22 5.598803E+8,    e23 5.827643E+8,    e24 6.054252E+8,    e25 6.278630E+8,    e26 6.500778E+8
e27 6.720695E+8,    e28 6.938382E+8,    e29 7.153839E+8,    e30 7.367064E+8,    e31 7.578059E+8,    e32 7.786824E+8,    e33 7.993358E+8,    e34 8.197661E+8,    e35 8.399734E+8,    e36 8.599577E+8,    e37 8.797188E+8,    e38 8.992570E+8,    e39 9.185720E+8
e40 9.376640E+8,    e41 9.565330E+8,    e42 9.751789E+8,    e43 9.936017E+8,    e44 1.011802E+9,    e45 1.029778E+9,    e46 1.047532E+9,    e47 1.065063E+9,    e48 1.082370E+9,    e49 1.099455E+9,    e50 1.116316E+9,    e51 1.132954E+9,    e52 1.149370E+9
e53 1.165562E+9,    e54 1.181531E+9,    e55 1.197277E+9,    e56 1.212801E+9,    e57 1.228101E+9,    e58 1.243178E+9,    e59 1.258032E+9,    e60 1.272662E+9,    e61 1.287070E+9,    e62 1.301255E+9,    e63 1.315217E+9,    e64 1.328956E+9,    e65 1.342471E+9
e66 1.355764E+9,    e67 1.368833E+9,    e68 1.381680E+9,    e69 1.394303E+9,    e70 1.406703E+9,    e71 1.418881E+9,    e72 1.430835E+9,    e73 1.442566E+9,    e74 1.454074E+9,    e75 1.465359E+9,    e76 1.476421E+9,    e77 1.487260E+9,    e78 1.497876E+9
e79 1.508269E+9,    e80 1.518439E+9"""

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
