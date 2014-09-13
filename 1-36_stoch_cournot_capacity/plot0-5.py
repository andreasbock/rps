#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  1.252816E+7,    e2  2.499902E+7,    e3  3.741260E+7,    e4  4.976888E+7,    e5  6.206788E+7,    e6  7.430959E+7,    e7  8.649401E+7,    e8  9.862113E+7,    e9  1.106910E+8,    e10 1.227035E+8,    e11 1.346588E+8,    e12 1.465568E+8,    e13 1.583974E+8
e14 1.701808E+8,    e15 1.819069E+8,    e16 1.935757E+8,    e17 2.051873E+8,    e18 2.167415E+8,    e19 2.282384E+8,    e20 2.396781E+8,    e21 2.510604E+8,    e22 2.623855E+8,    e23 2.736533E+8,    e24 2.848638E+8,    e25 2.960170E+8,    e26 3.071129E+8
e27 3.181516E+8,    e28 3.291329E+8,    e29 3.400569E+8,    e30 3.509237E+8,    e31 3.617332E+8,    e32 3.724853E+8,    e33 3.831802E+8,    e34 3.938178E+8,    e35 4.043981E+8,    e36 4.149212E+8,    e37 4.253869E+8,    e38 4.357953E+8,    e39 4.461465E+8
e40 4.564403E+8,    e41 4.666769E+8,    e42 4.768562E+8,    e43 4.869782E+8,    e44 4.970429E+8,    e45 5.070503E+8,    e46 5.170004E+8,    e47 5.268933E+8,    e48 5.367288E+8,    e49 5.465071E+8,    e50 5.562280E+8,    e51 5.658917E+8,    e52 5.754981E+8
e53 5.850472E+8,    e54 5.945390E+8,    e55 6.039735E+8,    e56 6.132283E+8,    e57 6.217096E+8,    e58 6.301041E+8,    e59 6.384121E+8,    e60 6.466333E+8,    e61 6.547680E+8,    e62 6.628160E+8,    e63 3.939790E+8,    e64 3.998532E+8,    e65 4.057154E+8
e66 4.115659E+8,    e67 4.174044E+8,    e68 4.232311E+8,    e69 4.290460E+8,    e70 4.348490E+8,    e71 4.406401E+8,    e72 4.464194E+8,    e73 4.521868E+8,    e74 4.579423E+8,    e75 4.636860E+8,    e76 4.694178E+8,    e77 4.751378E+8,    e78 4.808459E+8
e79 4.865422E+8,    e80 4.922266E+8"""

profit_n_raw ="""e1  1401105.947,    e2  2814663.789,    e3  4240673.525,    e4  5679135.155,    e5  7130048.679,    e6  8593414.098,    e7  1.006923E+7,    e8  1.155750E+7,    e9  1.305822E+7,    e10 1.457139E+7,    e11 1.609702E+7,    e12 1.763510E+7,    e13 1.918563E+7
e14 2.074861E+7,    e15 2.232404E+7,    e16 2.391192E+7,    e17 2.551226E+7,    e18 2.712505E+7,    e19 2.875029E+7,    e20 3.038798E+7,    e21 3.203812E+7,    e22 3.370072E+7,    e23 3.537577E+7,    e24 3.706327E+7,    e25 3.876322E+7,    e26 4.047562E+7
e27 4.220048E+7,    e28 4.393778E+7,    e29 4.568754E+7,    e30 4.744975E+7,    e31 4.922442E+7,    e32 5.101153E+7,    e33 5.281110E+7,    e34 5.462311E+7,    e35 5.644759E+7,    e36 5.828451E+7,    e37 6.013388E+7,    e38 6.199571E+7,    e39 6.386999E+7
e40 6.575672E+7,    e41 6.765590E+7,    e42 6.956753E+7,    e43 7.149162E+7,    e44 7.342815E+7,    e45 7.537714E+7,    e46 7.733858E+7,    e47 7.931248E+7,    e48 8.129882E+7,    e49 8.329762E+7,    e50 8.530887E+7,    e51 8.733257E+7,    e52 8.936872E+7
e53 9.141733E+7,    e54 9.347838E+7,    e55 9.555189E+7,    e56 9.774646E+7,    e57 1.005811E+8,    e58 1.034402E+8,    e59 1.063239E+8,    e60 1.092322E+8,    e61 1.121650E+8,    e62 1.151224E+8,    e63 3.922059E+8,    e64 3.918571E+8,    e65 3.915082E+8
e66 3.911594E+8,    e67 3.908106E+8,    e68 3.904618E+8,    e69 3.901131E+8,    e70 3.897643E+8,    e71 3.894154E+8,    e72 3.890666E+8,    e73 3.887178E+8,    e74 3.883690E+8,    e75 3.880203E+8,    e76 3.876714E+8,    e77 3.873226E+8,    e78 3.869738E+8
e79 3.866250E+8,    e80 3.862763E+8"""

rec_price_raw= """e1  159.504,    e2  159.008,    e3  158.512,    e4  158.016,    e5  157.520,    e6  157.024,    e7  156.528,    e8  156.032,    e9  155.536,    e10 155.040,    e11 154.544,    e12 154.048,    e13 153.552,    e14 153.056,    e15 152.560,    e16 152.064
e17 151.568,    e18 151.072,    e19 150.576,    e20 150.080,    e21 149.584,    e22 149.088,    e23 148.592,    e24 148.096,    e25 147.600,    e26 147.104,    e27 146.608,    e28 146.112,    e29 145.616,    e30 145.120,    e31 144.624,    e32 144.128
e33 143.632,    e34 143.136,    e35 142.640,    e36 142.144,    e37 141.648,    e38 141.152,    e39 140.656,    e40 140.160,    e41 139.664,    e42 139.168,    e43 138.672,    e44 138.176,    e45 137.680,    e46 137.184,    e47 136.688,    e48 136.192
e49 135.696,    e50 135.200,    e51 134.704,    e52 134.208,    e53 133.712,    e54 133.216,    e55 132.720,    e56 132.168,    e57 131.296,    e58 130.424,    e59 129.552,    e60 128.680,    e61 127.808,    e62 126.936"""

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
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,bbox_to_anchor=(0, 0.85),fancybox=False, shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
