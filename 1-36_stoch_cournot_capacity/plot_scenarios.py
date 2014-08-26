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

    legends = ['$q_r(\omega)$', '$q_n(\omega)$', '$P(Q(\omega))$', '$p_{REC}$']
    cols    = ['green', 'red', 'blue', 'purple']
    styles  = ['^', '--', 's', '-']

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
        ax1.set_ylabel(r'Quantities ($q_r(\omega)$, $q_n(\omega)$)')
        ax2.set_ylabel(r"Prices ($P(Q(\omega))$, $p_{REC}$)")

        my_plots = [None]*4

        #legends = ['$q_r$', '$q_n$', '$X_r$', '$\lambda$', '$p_{REC}$']
        for i in range(2):
            my_plots[i], = ax1.plot(rps, res[i][s], styles[i], c=cols[i], label=legends[i], linewidth=2)
        i=2
        my_plots[i], = ax2.plot(rps, res[i][s], styles[i], c=cols[i], label=legends[i], linewidth=2)
        for i in range(3,4):
            my_plots[i], = ax2.plot(rps, res[i], styles[i], c=cols[i], label=legends[i], linewidth=2)
                 
        ax1.legend(my_plots, legends, loc='upper center', bbox_to_anchor=(0.5, 1.125), fancybox=True, shadow=True, ncol=5)
        savefig(str(s)+'.png',bbox_inches='tight')

scenarios = 2

q_r_raw = """
a0      200.000     300.000
a1      200.000     300.000
a2      200.000     300.000
a3      200.000     300.000
a4      200.000     300.000
a5      200.000     300.000
a6      200.000     300.000
a7      200.000     300.000
a8      200.000     300.000
a9      200.000     300.000
a10     200.000     300.000
"""

q_n_raw = """
a0      500.000     500.000
a1      500.000     500.000
a2      500.000     500.000
a3      500.000     500.000
a4      398.533     350.914
a5      273.606     225.987
a6      190.320     142.701
a7      130.830      83.210
a8       86.211      38.592
a9       51.508       3.889
a10       0           0
"""

lda_raw = """
a0       93.000      92.000
a1       93.000      92.000
a2       93.000      92.000
a3       93.000      92.000
a4       94.015      93.491
a5       95.264      94.740
a6       96.097      95.573
a7       96.692      96.168
a8       97.138      96.614
a9       97.485      96.961
a10      98.000      97.000
"""

p_rec_raw = """
a4  174.077,    a5  144.509,    a6  123.339,    a7  107.504,    a8   95.237,    a9  85.465,    a10  78.501"""

q_r = parse(q_r_raw)
q_n = parse(q_n_raw)
lda = parse(lda_raw)
p_rec = parse_sgl(p_rec_raw)

res = [q_r, q_n, lda, p_rec]

plot_scenarios(scenarios, res)

