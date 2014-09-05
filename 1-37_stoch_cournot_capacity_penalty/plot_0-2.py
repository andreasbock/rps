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

profit_r_raw = """e1  3.467819E+7,    e2  6.911887E+7,    e3  1.033220E+8,    e4  1.372877E+8,    e5  1.710158E+8,    e6  2.045064E+8,    e7  2.377595E+8,    e8  2.707751E+8,    e9  3.035532E+8,    e10 3.360937E+8,    e11 3.683967E+8,    e12 4.004623E+8,    e13 4.322903E+8
e14 4.638807E+8,    e15 4.952337E+8,    e16 5.263492E+8,    e17 4.278348E+8,    e18 4.473509E+8,    e19 4.699474E+8,    e20 4.923063E+8,    e21 5.144277E+8,    e22 5.363116E+8,    e23 5.579579E+8,    e24 5.793668E+8,    e25 6.005381E+8,    e26 6.214719E+8
e27 6.421682E+8,    e28 6.626270E+8,    e29 6.828483E+8,    e30 7.028320E+8,    e31 7.225782E+8,    e32 7.420869E+8,    e33 7.613581E+8,    e34 7.803918E+8,    e35 7.991880E+8,    e36 8.177467E+8,    e37 8.360678E+8,    e38 8.541514E+8,    e39 8.719975E+8
e40 8.896061E+8,    e41 9.069772E+8,    e42 9.241107E+8,    e43 9.410068E+8,    e44 9.576653E+8,    e45 9.740863E+8,    e46 9.902698E+8,    e47 1.006216E+9,    e48 1.021924E+9,    e49 1.037395E+9,    e50 1.052629E+9"""

profit_n_raw ="""e1  1.866718E+9,    e2  1.846205E+9,    e3  1.825806E+9,    e4  1.805520E+9,    e5  1.785347E+9,    e6  1.765287E+9,    e7  1.745340E+9,    e8  1.725506E+9,    e9  1.705785E+9,    e10 1.686178E+9,    e11 1.666683E+9,    e12 1.647302E+9,    e13 1.628034E+9
e14 1.608879E+9,    e15 1.589837E+9,    e16 1.570908E+9,    e17 1.702299E+9,    e18 1.686665E+9,    e19 1.667205E+9,    e20 1.647859E+9,    e21 1.628625E+9,    e22 1.609505E+9,    e23 1.590498E+9,    e24 1.571604E+9,    e25 1.552823E+9,    e26 1.534155E+9
e27 1.515600E+9,    e28 1.497158E+9,    e29 1.478830E+9,    e30 1.460614E+9,    e31 1.442512E+9,    e32 1.424523E+9,    e33 1.406646E+9,    e34 1.388883E+9,    e35 1.371233E+9,    e36 1.353697E+9,    e37 1.336273E+9,    e38 1.318962E+9,    e39 1.301765E+9
e40 1.284680E+9,    e41 1.267709E+9,    e42 1.250851E+9,    e43 1.234105E+9,    e44 1.217473E+9,    e45 1.200954E+9,    e46 1.184549E+9,    e47 1.168256E+9,    e48 1.152076E+9,    e49 1.136010E+9,    e50 1.120056E+9"""

rec_price_raw="""e1  20.000,    e2  20.000,    e3  20.000,    e4  20.000,    e5  20.000,    e6  20.000,    e7  20.000,    e8  20.000,    e9  20.000,    e10 20.000,    e11 20.000,    e12 20.000,    e13 20.000,    e14 20.000,    e15 20.000,    e16 20.000,    e17  0.500"""

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

opt = str(sys.argv[1])
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

	x = 100*np.arange(1,51)

	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax2 = ax.twinx()
		ax2.set_ylabel(r"Prices ($p(\omega)$, $p_{REC}$)")
		power_prices1,  = ax2.plot(x,power_price.T[0],'--',c='black')
		#print power_price.T[0]; exit()
		power_prices2,  = ax2.plot(x,power_price.T[1],'.')
		rec_price_plot, = ax2.plot(x,rec_price,'x')
		ax.set_xlabel(r'Expected Renewable Capacity ($E_t[w^t]$)')
		ax.set_ylabel(r'Profit of the producers')
		if one_dim:
			profit_r_plt,= ax.plot(x,profit_r,'s')
			profit_n_plt,= ax.plot(x,profit_n)
		else:
			profit,= ax.plot(x,z.T[int(a*10)])
		#ax.legend([profit_r_plt,power_prices1,power_prices2], ["Profit","Power price, scenario 1 (high)", "Power price, scenario 2 (low)"], loc='upper center', bbox_to_anchor=(0, -0.125),fancybox=True, shadow=True, ncol=5)
		ax.legend([profit_r_plt,profit_n_plt,power_prices1,power_prices2,rec_price_plot], ["$\Xi_r$","$\Xi_n$","$p_e^1$","$p_e^2$", "$p_{REC}$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("foo.svg",bbox_inches='tight')

	for a in alphas:
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.set_xlabel(r'Expected Renewable Capacity ($E_t[w^t]$)')
		ax.set_ylabel(r"Quantities ($q_r^t$, $q_n^t$)")
		q_r_plt1, = ax.plot(x,q_r.T[0],'--',c='green')
		q_r_plt2, = ax.plot(x,q_r.T[1],'.',c='green')
		q_n_plt1, = ax.plot(x,q_r.T[0],'x',c='black')
		q_n_plt2, = ax.plot(x,q_r.T[1],'k',c='black')

		ax.legend([q_r_plt1, q_r_plt2, q_n_plt1, q_n_plt2], ["$q_r^1$","$q_r^2$","$q_n^1$","$q_n^2$"], loc='upper center', bbox_to_anchor=(0.5, -0.125),fancybox=True, shadow=True, ncol=5)
		fig.savefig("fooprod.svg",bbox_inches='tight')
