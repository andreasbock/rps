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
styles   = ['^', '--', 's', '4']
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

res = []
for line in lines:
    if line and line.startswith("i") and line[1].isdigit():
        res.append(parse_result(line.split()))
        #if idx < 1:
            #my_plots[idx], = ax1.plot(rps, res, c=cols[idx], label=legends[idx], linewidth=2)
        #else:
            ##idx += 1
            #my_plots[idx], = ax2.plot(rps, res, c=cols[idx], label=legends[idx], linewidth=2)
        #idx += 1

for idx in [0,1]:
    my_plots[idx], = ax1.plot(rps, res[idx],styles[idx], c=cols[idx], label=legends[idx], linewidth=2)
idx=2

my_plots[idx], = ax1.plot(rps, [0.0]*11,styles[idx], c=cols[idx], label=legends[idx], linewidth=2)

for idx in [3]:
    my_plots[idx], = ax2.plot(rps, res[idx-1],styles[idx], c=cols[idx], label=legends[idx], linewidth=2)
    
#ax1.legend([my_plots[0]], [legends[0]], 'upper left')
#ax2.legend(my_plots[1:], legends[1:], 'upper right')

ax1.legend(my_plots, legends, loc='upper center', bbox_to_anchor=(0.5, 1.125),fancybox=True, shadow=True, ncol=5)

savefig('foo.png',bbox_inches='tight')
