#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

power_price_raw="""e1       63.495      63.600
e2       63.181      63.390
e3       62.867      63.181
e4       62.552      62.971
e5       62.238      62.762
e6       61.924      62.552
e7       61.610      62.343
e8       61.295      62.133
e9       60.981      61.924
e10      60.667      61.714
e11      60.352      61.505
e12      60.038      61.295
e13      59.724      61.086
e14      59.410      60.876
e15      59.095      60.667
e16      58.781      60.457
e17      56.610      58.390
e18      56.248      58.133
e19      55.933      57.924
e20      55.619      57.714
e21      55.305      57.505
e22      54.990      57.295
e23      54.676      57.086
e24      54.362      56.876
e25      54.048      56.667
e26      53.733      56.457
e27      53.419      56.248
e28      53.105      56.038
e29      52.790      55.829
e30      52.476      55.619
e31      52.162      55.410
e32      51.848      55.200
e33      51.533      54.990
e34      51.219      54.781
e35      50.905      54.571
e36      50.590      54.362
e37      50.276      54.152
e38      49.962      53.943
e39      49.648      53.733
e40      49.333      53.524
e41      49.019      53.314
e42      48.705      53.105
e43      48.390      52.895
e44      48.076      52.686
e45      47.762      52.476
e46      47.448      52.267
e47      47.133      52.057
e48      46.819      51.848
e49      46.505      51.638
e50      46.190      51.429"""

profit_r_raw = """e1  9293470.927,    e2  1.805637E+7,    e3  2.628869E+7,    e4  3.399044E+7,    e5  4.116161E+7,    e6  4.780221E+7,    e7  5.391223E+7,    e8  5.949168E+7,    e9  6.454055E+7,    e10 6.905885E+7,    e11 7.304658E+7,    e12 7.650373E+7,    e13 7.943030E+7
e14 8.182630E+7,    e15 8.369173E+7,    e16 8.501607E+7,    e17 8.604688E+7,    e18 8.691445E+7,    e19 8.761876E+7,    e20 8.815981E+7,    e21 8.853761E+7,    e22 8.875216E+7,    e23 8.880346E+7,    e24 8.868098E+7,    e25 8.851598E+7,    e26 8.835098E+7
e27 8.818598E+7,    e28 8.802098E+7,    e29 8.785598E+7,    e30 8.769098E+7,    e31 8.752598E+7,    e32 8.736098E+7,    e33 8.719598E+7,    e34 8.703098E+7,    e35 8.686598E+7,    e36 8.670098E+7,    e37 8.653598E+7,    e38 8.637098E+7,    e39 8.620598E+7
e40 8.604098E+7,    e41 8.587598E+7,    e42 8.571098E+7,    e43 8.554598E+7,    e44 8.538098E+7,    e45 8.521598E+7,    e46 8.505098E+7,    e47 8.488598E+7,    e48 8.472098E+7,    e49 8.455598E+7,    e50 8.439098E+7"""

profit_n_raw ="""e1  1.865358E+7,    e2  3.677658E+7,    e3  5.436901E+7,    e4  3.399044E+7,    e5  4.116161E+7,    e6  4.780221E+7,    e7  5.391223E+7,    e8  5.949168E+7,    e9  6.454055E+7,    e10 6.905885E+7,    e11 7.304658E+7,    e12 7.650373E+7,    e13 7.943030E+7
e14 8.182630E+7,    e15 8.369173E+7,    e16 8.501607E+7,    e17 8.604688E+7,    e18 8.691445E+7,    e19 8.761876E+7,    e20 8.815981E+7,    e21 8.853761E+7,    e22 8.875216E+7,    e23 8.880346E+7,    e24 8.868098E+7,    e25 8.851598E+7,    e26 8.835098E+7
e27 8.818598E+7,    e28 8.802098E+7,    e29 8.785598E+7,    e30 8.769098E+7,    e31 8.752598E+7,    e32 8.736098E+7,    e33 8.719598E+7,    e34 8.703098E+7,    e35 8.686598E+7,    e36 8.670098E+7,    e37 8.653598E+7,    e38 8.637098E+7,    e39 8.620598E+7
e40 8.604098E+7,    e41 8.587598E+7,    e42 8.571098E+7,    e43 8.554598E+7,    e44 8.538098E+7,    e45 8.521598E+7,    e46 8.505098E+7,    e47 8.488598E+7,    e48 8.472098E+7,    e49 8.455598E+7,    e50 8.439098E+7"""

rec_price_raw="""e1  20.000,    e2  20.000,    e3  20.000"""
#rec_price_raw="""e1  20.000,    e2  20.000,    e3  20.000,    e4  20.000,    e5  20.000,    e6  20.000,    e7  20.000,    e8  20.000,    e9  20.000,    e10 20.000,    e11 20.000,    e12 20.000,    e13 20.000,    e14 20.000,    e15 20.000,    e16 20.000,    e17  0.500"""

prod_r_raw="""e1       60.000      40.000
e2      120.000      80.000
e3      180.000     120.000
e4      240.000     160.000
e5      300.000     200.000
e6      360.000     240.000
e7      420.000     280.000
e8      480.000     320.000
e9      540.000     360.000
e10     600.000     400.000
e11     660.000     440.000
e12     720.000     480.000
e13     780.000     520.000
e14     840.000     560.000
e15     900.000     600.000
e16     960.000     640.000
e17    1020.000     680.000
e18    1080.000     720.000
e19    1140.000     760.000
e20    1200.000     800.000
e21    1260.000     840.000
e22    1320.000     880.000
e23    1380.000     920.000
e24    1440.000     960.000
e25    1500.000    1000.000
e26    1560.000    1040.000
e27    1620.000    1080.000
e28    1680.000    1120.000
e29    1740.000    1160.000
e30    1800.000    1200.000
e31    1860.000    1240.000
e32    1920.000    1280.000
e33    1980.000    1320.000
e34    2040.000    1360.000
e35    2100.000    1400.000
e36    2160.000    1440.000
e37    2220.000    1480.000
e38    2280.000    1520.000
e39    2340.000    1560.000
e40    2400.000    1600.000
e41    2460.000    1640.000
e42    2520.000    1680.000
e43    2580.000    1720.000
e44    2640.000    1760.000
e45    2700.000    1800.000
e46    2760.000    1840.000
e47    2820.000    1880.000
e48    2880.000    1920.000
e49    2940.000    1960.000
e50    3000.000    2000.000"""

prod_n_raw="""e1     3590.476    3600.000
e2     3561.905    3580.952
e3     3533.333    3561.905
e4     3504.762    3542.857
e5     3476.190    3523.810
e6     3447.619    3504.762
e7     3419.048    3485.714
e8     3390.476    3466.667
e9     3361.905    3447.619
e10    3333.333    3428.571
e11    3304.762    3409.524
e12    3276.190    3390.476
e13    3247.619    3371.429
e14    3219.048    3352.381
e15    3190.476    3333.333
e16    3161.905    3314.286
e17    3319.048    3480.952
e18    3295.238    3466.667
e19    3266.667    3447.619
e20    3238.095    3428.571
e21    3209.524    3409.524
e22    3180.952    3390.476
e23    3152.381    3371.429
e24    3123.810    3352.381
e25    3095.238    3333.333
e26    3066.667    3314.286
e27    3038.095    3295.238
e28    3009.524    3276.190
e29    2980.952    3257.143
e30    2952.381    3238.095
e31    2923.810    3219.048
e32    2895.238    3200.000
e33    2866.667    3180.952
e34    2838.095    3161.905
e35    2809.524    3142.857
e36    2780.952    3123.810
e37    2752.381    3104.762
e38    2723.810    3085.714
e39    2695.238    3066.667
e40    2666.667    3047.619
e41    2638.095    3028.571
e42    2609.524    3009.524
e43    2580.952    2990.476
e44    2552.381    2971.429
e45    2523.810    2952.381
e46    2495.238    2933.333
e47    2466.667    2914.286
e48    2438.095    2895.238
e49    2409.524    2876.190
e50    2380.952    2857.143"""

one_dim = True

opt ="2d"
rc('text',usetex=True)
rc('font',family='serif')


if one_dim:
	profit_r = np.zeros(shape=(50))
	i = 0
	for p_raw in profit_r_raw.split('\n'):
		for p_raw2 in p_raw.split(','):
			profit_r[i] = float(p_raw2.split()[1])
			i+=1

	profit_n = np.zeros(shape=(50))
	i = 0
	for p_raw in profit_n_raw.split('\n'):
		for p_raw2 in p_raw.split(','):
			profit_n[i] = float(p_raw2.split()[1])
			i+=1

comb = zip(profit_r,100*np.arange(1,51))
max = float("-inf")
res = None
for (p,r) in comb:
	if max < p:
		max = p; res=r

print res

power_price = np.zeros(shape=(50,2))

i = 0
for p_raw in power_price_raw.split('\n'):
    p = p_raw.split()[1:]
    power_price[i] = np.array(map(float, p))
    i +=1

rec_price = np.zeros(shape=(50))

i = 0
for p_raw in rec_price_raw.split('\n'):
	for p_raw2 in p_raw.split(','):
		rec_price[i] = float(p_raw2.split()[1])
		i+=1

q_r = np.zeros(shape=(50,2))

i = 0
for p_raw in prod_r_raw.split('\n'):
    p = p_raw.split()[1:]
    q_r[i] = np.array(map(float, p))
    i +=1
q_n = np.zeros(shape=(50,2))
i = 0
for p_raw in prod_n_raw.split('\n'):
    p = p_raw.split()[1:]
    q_n[i] = np.array(map(float, p))
    i +=1

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
	alphas = [0.5]

	x = 55*np.arange(2,52)

	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.grid(True)
		ax2 = ax.twinx()
		ax2.set_ylabel(r"Prices ($p(\omega)$, $p_{REC}$)")
		#power_prices1,  = ax2.plot(x,power_price.T[0],'--',c='black')
		#print power_price.T[0]; exit()
		#power_prices2,  = ax2.plot(x,power_price.T[1],'.')
		rec_price_plot, = ax2.plot(x,rec_price,'x')
		ax.set_xlabel(r'Installed Capacity ($w$)')
		ax.set_ylabel(r'Profit of the producers')
		if one_dim:
			profit_r_plt,= ax.plot(x,profit_r,'s')
			profit_n_plt,= ax.plot(x,profit_n)
		else:
			profit,= ax.plot(x,z.T[int(a*10)])
		#ax.legend([profit_r_plt,power_prices1,power_prices2], ["Profit","Power price, scenario 1 (high)", "Power price, scenario 2 (low)"], loc='upper center', bbox_to_anchor=(0, -0.125),fancybox=True, shadow=True, ncol=5)
		#ax.legend([profit_r_plt,profit_n_plt,power_prices1,power_prices2,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_e^1$","$p_e^2$", "$p_{REC}$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], [r"$\Xi_r$, 0\% RPS",r"$\Xi_r$, 20\% RPS",r"$p_{REC}$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
#		ax.legend([profit_r_plt,profit_n_plt,rec_price_plot], ["$\Xi_r$,$\alpha=0$","$\Xi_r$,$\alpha=0.2$","$p_e^1$","$p_e^2$", "$p_{REC}$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("foo2.png",bbox_inches='tight')
		print "here"
	exit()
	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.grid(True)
		ax.set_xlabel(r'Expected Renewable Capacity ($E_t[w^t]$)')
		ax.set_ylabel(r"Quantities ($q_r^t$, $q_n^t$)")
		q_r_plt1, = ax.plot(x,q_r.T[0],'--',c='green')
		q_r_plt2, = ax.plot(x,q_r.T[1],'.',c='green')
		q_n_plt1, = ax.plot(x,q_n.T[0],'x',c='black')
		q_n_plt2, = ax.plot(x,q_n.T[1],'k',c='black')

		ax.legend([q_r_plt1, q_r_plt2, q_n_plt1, q_n_plt2], ["$q_r^1$","$q_r^2$","$q_n^1$","$q_n^2$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("fooprod.png",bbox_inches='tight')
