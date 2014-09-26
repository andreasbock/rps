#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  7836470.914,    e2  1.564988E+7,    e3  2.344024E+7,    e4  3.120753E+7,    e5  3.895177E+7,    e6  4.667295E+7,    e7  5.437107E+7,    e8  6.204614E+7,    e9  6.969814E+7,    e10 7.732709E+7,    e11 8.493298E+7,    e12 9.251581E+7,    e13 1.000756E+8
e14 1.076123E+8,    e15 1.151260E+8,    e16 1.226166E+8,    e17 1.300841E+8,    e18 1.375286E+8,    e19 1.449500E+8,    e20 1.523484E+8,    e21 1.597237E+8,    e22 1.670759E+8,    e23 1.744051E+8,    e24 1.817112E+8,    e25 1.889943E+8,    e26 1.962543E+8
e27 2.034913E+8,    e28 2.107052E+8,    e29 2.178960E+8,    e30 2.250638E+8,    e31 2.322085E+8,    e32 2.393302E+8,    e33 2.464288E+8,    e34 2.535044E+8,    e35 2.605569E+8,    e36 2.675863E+8,    e37 2.745927E+8,    e38 2.815760E+8,    e39 2.885363E+8
e40 2.954735E+8,    e41 3.023876E+8,    e42 3.092787E+8,    e43 3.161467E+8,    e44 3.229917E+8,    e45 3.298136E+8,    e46 3.366125E+8,    e47 3.433882E+8,    e48 3.501410E+8,    e49 3.568707E+8,    e50 3.635773E+8,    e51 3.702608E+8,    e52 3.769214E+8
e53 3.835588E+8,    e54 3.901732E+8,    e55 3.967645E+8,    e56 4.033328E+8,    e57 4.098780E+8,    e58 4.164002E+8,    e59 4.228993E+8,    e60 4.293753E+8,    e61 4.358283E+8,    e62 4.422582E+8,    e63 4.486651E+8,    e64 4.550489E+8,    e65 4.614096E+8
e66 4.677473E+8,    e67 4.740619E+8,    e68 4.803535E+8,    e69 4.866220E+8,    e70 4.928675E+8,    e71 4.990899E+8,    e72 5.052892E+8,    e73 5.114655E+8,    e74 5.176187E+8,    e75 5.237489E+8,    e76 5.298560E+8,    e77 5.359401E+8,    e78 5.420010E+8
e79 5.480390E+8,    e80 5.540539E+8"""

profit_n_raw ="""e1   874393.782,    e2  1753975.129,    e3  2638744.039,    e4  3528700.514,    e5  4423844.554,    e6  5324176.157,    e7  6229695.325,    e8  7140402.057,    e9  8056296.354,    e10 8977378.214,    e11 9903647.639,    e12 1.083510E+7,    e13 1.177175E+7
e14 1.271358E+7,    e15 1.366060E+7,    e16 1.461281E+7,    e17 1.557020E+7,    e18 1.653279E+7,    e19 1.750056E+7,    e20 1.847351E+7,    e21 1.945166E+7,    e22 2.043499E+7,    e23 2.142351E+7,    e24 2.241722E+7,    e25 2.341611E+7,    e26 2.442020E+7
e27 2.542947E+7,    e28 2.644393E+7,    e29 2.746357E+7,    e30 2.848840E+7,    e31 2.951842E+7,    e32 3.055363E+7,    e33 3.159403E+7,    e34 3.263961E+7,    e35 3.369038E+7,    e36 3.474634E+7,    e37 3.580749E+7,    e38 3.687382E+7,    e39 3.794534E+7
e40 3.902205E+7,    e41 4.010395E+7,    e42 4.119103E+7,    e43 4.228330E+7,    e44 4.338076E+7,    e45 4.448341E+7,    e46 4.559124E+7,    e47 4.670426E+7,    e48 4.782247E+7,    e49 4.894587E+7,    e50 5.007446E+7,    e51 5.120823E+7,    e52 5.234719E+7
e53 5.349133E+7,    e54 5.464067E+7,    e55 5.579519E+7,    e56 5.695490E+7,    e57 5.811980E+7,    e58 5.928988E+7,    e59 6.046516E+7,    e60 6.164562E+7,    e61 6.283126E+7,    e62 6.402210E+7,    e63 6.521812E+7,    e64 6.641933E+7,    e65 6.762573E+7
e66 6.883732E+7,    e67 7.005409E+7,    e68 7.127605E+7,    e69 7.250320E+7,    e70 7.373553E+7,    e71 7.497306E+7,    e72 7.621577E+7,    e73 7.746367E+7,    e74 7.871675E+7,    e75 7.997502E+7,    e76 8.123849E+7,    e77 8.250713E+7,    e78 8.378097E+7
e79 8.505999E+7,    e80 8.634421E+7"""

rec_price_raw= """e1  159.690,    e2  159.380,    e3  159.070,    e4  158.760,    e5  158.450,    e6  158.140,    e7  157.830,    e8  157.520,    e9  157.210,    e10 156.900,    e11 156.590,    e12 156.280,    e13 155.970,    e14 155.660,    e15 155.350,    e16 155.040
e17 154.730,    e18 154.420,    e19 154.110,    e20 153.800,    e21 153.490,    e22 153.180,    e23 152.870,    e24 152.560,    e25 152.250,    e26 151.940,    e27 151.630,    e28 151.320,    e29 151.010,    e30 150.700,    e31 150.390,    e32 150.080
e33 149.770,    e34 149.460,    e35 149.150,    e36 148.840,    e37 148.530,    e38 148.220,    e39 147.910,    e40 147.600,    e41 147.290,    e42 146.980,    e43 146.670,    e44 146.360,    e45 146.050,    e46 145.740,    e47 145.430,    e48 145.120
e49 144.810,    e50 144.500,    e51 144.190,    e52 143.880,    e53 143.570,    e54 143.260,    e55 142.950,    e56 142.640,    e57 142.330,    e58 142.020,    e59 141.710,    e60 141.400,    e61 141.090,    e62 140.780,    e63 140.470,    e64 140.160
e65 139.850,    e66 139.540,    e67 139.230,    e68 138.920,    e69 138.610,    e70 138.300,    e71 137.990,    e72 137.680,    e73 137.370,    e74 137.060,    e75 136.750,    e76 136.440,    e77 136.130,    e78 135.820,    e79 135.510,    e80 135.200"""

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
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_{REC}$"], loc='upper left',frameon=False,bbox_to_anchor=(0.3, 1),fancybox=False, shadow=False, ncol=5) #bbox_to_anchor=(0.5, -0.125)
		#fig.show()
		fig.savefig("foo.svg",bbox_inches='tight')
