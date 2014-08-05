#!/usr/bin/python2
from pylab import *
import numpy as np
import sys

filename = str(sys.argv[1])

f = open(filename)
lines = f.readlines()
f.close()

def parse_result(line):
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

legends = ['$q_r$', '$q_n$', '$p_{REC}$', '$p$']
cols   = ['green', 'red', 'blue', 'purple']
styles   = ['^', '--', 's', '-']
rps    = np.arange(0,1.1,0.1)

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



my_plots = [None]*4

q_r = np.zeros(11)
q_n = np.zeros(11)
pz=[None,None]

idx = 0
for line in lines:
    if line and line.startswith("i") and line[1].isdigit():
        res = parse_result(line.split())
        if idx < 2:
            my_plots[idx], = ax1.plot(rps, res, styles[idx], c=cols[idx], label=legends[idx], linewidth=2)
            pz[idx]=res
        else:
            idx += 1
            my_plots[idx], = ax2.plot(rps, res, styles[idx], c=cols[idx], label=legends[idx], linewidth=2)
            break
        idx += 1
debug=0
if debug:
    total = np.zeros(11)
    for i in range(11):
        total[i]=(1-float(i)/10.0)*pz[0][i] - float(i)/10.0*pz[1][i]

    for i in total:
        print i
    exit()

idx=2
my_plots[idx], = ax2.plot(rps, [0.0]*11, styles[idx], c=cols[idx], label=legends[idx], linewidth=2)

#ax1.legend(my_plots[:2], legends[:2], 'upper left')
#ax2.legend(my_plots[2:], legends[2:], 'upper right')
ax1.legend(my_plots, legends, loc='upper center', bbox_to_anchor=(0.5, -0.1),fancybox=True, shadow=True, ncol=5)

savefig('foo.png',bbox_inches='tight')


