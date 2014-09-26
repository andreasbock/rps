#!/usr/bin/python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,rc
import numpy as np
import sys

profit_raw   =""""""

profit_r_raw = """e1  4355228.914,    e2  8700915.657,    e3  1.303706E+7,    e4  1.736366E+7,    e5  2.168072E+7,    e6  2.598824E+7,    e7  3.028622E+7,    e8  3.457465E+7,    e9  3.885354E+7,    e10 4.312289E+7,    e11 4.738270E+7,    e12 5.163296E+7,    e13 5.587369E+7
e14 6.010487E+7,    e15 6.432651E+7,    e16 6.853860E+7,    e17 7.274116E+7,    e18 7.693417E+7,    e19 8.111764E+7,    e20 8.529157E+7,    e21 8.945595E+7,    e22 9.361079E+7,    e23 9.775610E+7,    e24 1.018919E+8,    e25 1.060181E+8,    e26 1.101347E+8
e27 1.142419E+8,    e28 1.183395E+8,    e29 1.224275E+8,    e30 1.265060E+8,    e31 1.305750E+8,    e32 1.346344E+8,    e33 1.386843E+8,    e34 1.427246E+8,    e35 1.467554E+8,    e36 1.507767E+8,    e37 1.547884E+8,    e38 1.587906E+8,    e39 1.627832E+8
e40 1.667663E+8,    e41 1.707398E+8,    e42 1.747038E+8,    e43 1.786583E+8,    e44 1.826032E+8,    e45 1.865386E+8,    e46 1.904644E+8,    e47 1.943807E+8,    e48 1.982874E+8,    e49 2.021846E+8,    e50 2.060723E+8,    e51 2.099504E+8,    e52 2.138190E+8
e53 2.176780E+8,    e54 2.215275E+8,    e55 2.253675E+8,    e56 2.291979E+8,    e57 2.330187E+8,    e58 2.368301E+8,    e59 2.406319E+8,    e60 2.444241E+8,    e61 2.482068E+8,    e62 2.519799E+8,    e63 2.557436E+8,    e64 2.594976E+8,    e65 2.632422E+8
e66 2.669772E+8,    e67 2.707026E+8,    e68 2.744185E+8,    e69 2.781249E+8,    e70 2.818217E+8,    e71 2.855090E+8,    e72 2.891867E+8,    e73 2.928549E+8,    e74 2.965135E+8,    e75 3.001626E+8,    e76 3.038022E+8,    e77 3.074322E+8,    e78 3.110527E+8
e79 3.146637E+8,    e80 3.182651E+8"""

profit_n_raw ="""e1  4355635.782,    e2  8702943.129,    e3  1.304192E+7,    e4  1.737257E+7,    e5  2.169489E+7,    e6  2.600889E+7,    e7  3.031455E+7,    e8  3.461189E+7,    e9  3.890090E+7,    e10 4.318158E+7,    e11 4.745393E+7,    e12 5.171795E+7,    e13 5.597365E+7
e14 6.022101E+7,    e15 6.446005E+7,    e16 6.869076E+7,    e17 7.291314E+7,    e18 7.712719E+7,    e19 8.133292E+7,    e20 8.553031E+7,    e21 8.971938E+7,    e22 9.390012E+7,    e23 9.807253E+7,    e24 1.022366E+8,    e25 1.063924E+8,    e26 1.105398E+8
e27 1.146789E+8,    e28 1.188097E+8,    e29 1.229321E+8,    e30 1.270462E+8,    e31 1.311520E+8,    e32 1.352494E+8,    e33 1.393386E+8,    e34 1.434194E+8,    e35 1.474918E+8,    e36 1.515560E+8,    e37 1.556118E+8,    e38 1.596593E+8,    e39 1.636984E+8
e40 1.677293E+8,    e41 1.717517E+8,    e42 1.757659E+8,    e43 1.797718E+8,    e44 1.837693E+8,    e45 1.877585E+8,    e46 1.917393E+8,    e47 1.957118E+8,    e48 1.996760E+8,    e49 2.036319E+8,    e50 2.075795E+8,    e51 2.115187E+8,    e52 2.154496E+8
e53 2.193721E+8,    e54 2.232863E+8,    e55 2.271922E+8,    e56 2.310898E+8,    e57 2.349791E+8,    e58 2.388600E+8,    e59 2.427326E+8,    e60 2.465968E+8,    e61 2.504527E+8,    e62 2.543003E+8,    e63 2.581396E+8,    e64 2.619706E+8,    e65 2.657932E+8
e66 2.696075E+8,    e67 2.734134E+8,    e68 2.772111E+8,    e69 2.810004E+8,    e70 2.847813E+8,    e71 2.885540E+8,    e72 2.923183E+8,    e73 2.960743E+8,    e74 2.998219E+8,    e75 3.035613E+8,    e76 3.072923E+8,    e77 3.110150E+8,    e78 3.147293E+8
e79 3.184353E+8,    e80 3.221330E+8"""

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
