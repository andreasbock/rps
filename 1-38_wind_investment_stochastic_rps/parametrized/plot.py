#!/usr/bin/python
from pylab import *
import numpy as np
import sys

rps     = np.arange(0,1.1,0.1)
rps_rng = len(rps)

def parse(q):
	res = np.zeros(shape=(scenarios, rps_rng))
	q_l = q.split('\n')
	for l in q_l:
		vals = l.split()
		if not l: continue
		rps_index = vals[0][1:]
		for s in range(scenarios):
			res[s,rps_index] = vals[s+1]
	return res

def parse_sgl(line):
	line = line.split()
	result = [0]*11
	count = 1
	i = 0
	while count <= len(line)/2:
		dgt = line[i][1:]
		if line[i].startswith("i") and dgt.isdigit():
			if i==len(line)-2:
				result[int(dgt)-1] = (float(line[i+1]))
			else:
				result[int(dgt)-1] = (float(line[i+1][:-1]))
		i += 2
		count +=1
	return result

def plot_scenarios(scenarios, res):

    legends = ['$q_r$', '$q_n$', '$\lambda$', '$p_{REC}$', '$X_r$']
    cols    = ['green', 'red', 'blue', 'purple','black']
    styles  = ['^', '--', 's', '-','.']

    for s in range(scenarios):
        fig, ax1 = subplots()

        rc('text',usetex=True)
        rc('font',family='serif')

        ax2 = ax1.twinx()

        ax1.spines['top'].set_visible(False)
        ax1.spines['bottom'].set_smart_bounds(True)
        ax2.spines['top'].set_visible(False)
        ax2.spines['bottom'].set_smart_bounds(True)

        for loc, spine in ax1.spines.items():
            if loc in ['left','bottom','right']:
                    spine.set_position(('outward',10)) # outward by 10 points

        for loc, spine in ax2.spines.items():
            if loc in ['left','bottom','right']:
                    spine.set_position(('outward',10)) # outward by 10 points

        ax1.grid(True)

        ax1.set_xlabel(r'RPS level ($\alpha$)')
        ax1.set_ylabel(r'Quantities ($q_r$, $q_n$)')
        ax2.set_ylabel(r"Prices ($p$, $p_{REC}$)")

        my_plots = [None]*5

        #legends = ['$q_r$', '$q_n$', '$X_r$', '$\lambda$', '$p_{REC}$']
        for i in range(3):
            my_plots[i], = ax1.plot(rps, res[i][s], styles[i], c=cols[i], label=legends[i], linewidth=2)
        for i in range(3,5):
            my_plots[i], = ax1.plot(rps, res[i], styles[i], c=cols[i], label=legends[i], linewidth=2)
                 
        ax1.legend(my_plots, legends, loc='upper center', bbox_to_anchor=(0.5, 1.125), fancybox=True, shadow=True, ncol=5)
        savefig(str(s)+'.png',bbox_inches='tight')

scenarios = 2

q_r_raw = """
i1      499.500     333.000
i2      499.500     333.000
i3      499.500     333.000
i4      240.000     160.000
i5      300.000     200.000
i6      360.000     240.000
i7      420.000     280.000
i8      480.000     320.000
i9      500.000     400.000
i10     500.000     500.000
"""

q_n_raw = """
i0     500.000     500.000
i1       0.500     167.000
i2       0.500     167.000
i3       0.500     167.000
i4     260.000     340.000
i5     200.000     300.000
i6     140.000     260.000
i7      80.000     220.000
i8      20.000     180.000
i9           0     100.000
"""

r_inst_raw = """i1  333.000,    i2  333.000,    i3  333.000,    i4  160.000,    i5  200.000,    i6  240.000,    i7  280.000,    i8  320.000,    i9  400.000,    i10 500.000
"""

lda_raw = """
i0       20.500      20.500
i1       20.000      20.167
i2       20.000      20.167
i3       20.000      20.167
i4       20.260      20.340
i5       20.200      20.300
i6       20.140      20.260
i7       20.080      20.220
i8       20.020      20.180
i9            0      20.100
i10           0      20.000
"""

p_rec_raw = """
i4  183.438,    i5  149.500,    i6  126.111,    i7  109.031,    i8   96.016,    i9   85.772,    i10  77.500
"""

q_r = parse(q_r_raw)
q_n = parse(q_n_raw)
r_inst = parse_sgl(r_inst_raw)
lda = parse(lda_raw)
p_rec = parse_sgl(p_rec_raw)

res = [q_r, q_n, lda, p_rec, r_inst]

plot_scenarios(scenarios, res)

