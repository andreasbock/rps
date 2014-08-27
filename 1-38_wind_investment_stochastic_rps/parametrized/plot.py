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
        if (line[i].startswith("i") or line[i].startswith("a")) and dgt.isdigit():
            #print line[i+1]
            if i==len(line)-2:
                result[int(dgt)] = (float(line[i+1]))
            else:
                result[int(dgt)] = (float(line[i+1][:-1]))
        i += 2
        count +=1
    return result

def plot_scenarios(scenarios, res):

    legends = ['$q_r$', '$q_n$', '$\lambda$', '$p_{REC}$', '$X_r$']
    cols    = ['green', 'red', 'blue', 'purple','black']
    styles  = ['^', '--', 's', '-','*']

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
        ax1.set_ylabel(r'Quantities ($q_r$, $q_n$, $X_r$)')
        ax2.set_ylabel(r"Prices ($\lambda$, $p_{REC}$)")

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
a0      600.000     360.000
a1       75.000      45.000
a2      150.000      90.000
a3      225.000     135.000
a4      300.000     180.000
a5      375.000     225.000
a6      450.000     270.000
a7      525.000     315.000
a8      600.000     360.000
a9      600.000     540.000
a10     600.000     540.000
"""

q_n_raw = """
a0            0     240.000
a1      525.000     555.000
a2      450.000     510.000
a3      375.000     465.000
a4      300.000     420.000
a5      225.000     375.000
a6      150.000     330.000
a7       75.000     285.000
a8            0     240.000
a9            0      60.000
a10           0      60.000
"""

r_inst_raw = """a0  400.000,    a1   50.000,    a2  100.000,    a3  150.000,    a4  200.000,    a5  250.000,    a6  300.000,    a7  350.000,    a8  400.000,    a9  600.000,    a10 600.000
"""

lda_raw = """
i0       20.000      20.240
i1       20.525      20.555
i2       20.450      20.510
i3       20.375      20.465
i4       20.300      20.420
i5       20.225      20.375
i6       20.150      20.330
i7       20.075      20.285
i8       20.000      20.240
i9            0      20.060
i10           0      20.060
"""

p_rec_raw = """a1 2000.000,    a2 2000.000,    a3 2000.000,    a4 2000.000,    a5 2000.000,    a6 2000.000, a7 2000.000,    a8 2000.000"""

q_r = parse(q_r_raw)
q_n = parse(q_n_raw)
r_inst = parse_sgl(r_inst_raw)
lda = parse(lda_raw)
p_rec = parse_sgl(p_rec_raw)

res = [q_r, q_n, lda, p_rec, r_inst]

plot_scenarios(scenarios, res)

