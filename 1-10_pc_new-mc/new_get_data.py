#!/usr/bin/python2
from pylab import *
import numpy as np
import sys

filename = str(sys.argv[1])

f = open(filename)
lines = f.readlines()
f.close()

def parse_result(line):
    result = [0.0]*11
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

legends = ['q_r', 'q_n', 'p_rec', 'p']
cols   = ['green', 'red', 'blue', 'purple']
styles = ['^', '--', 's', '']
rps    = np.arange(0,1.1,0.1)

#figure()
#subplot(111)

fig, ax1 = subplots()

ax1.set_xlabel('RPS level')
ax1.set_ylabel('Quantities')

ax2 = ax1.twinx()
ax2.set_ylabel('Price')

ax1.grid(True)

my_plots = [None]*4

idx = 0
for line in lines:
    if line and line.startswith("i") and line[1].isdigit():
        res = parse_result(line.split())
        if idx < 3:
            my_plots[idx], = ax1.plot(rps, res, styles[idx], c=cols[idx], label=legends[idx], linewidth=2)
            break
        else:
            my_plots[idx], = ax2.plot(rps, res, styles[idx], c=cols[idx], label=legends[idx], linewidth=2)
        idx += 1

ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

my_plots[1], = ax1.plot(rps, [0.0]*11, styles[1], c=cols[1], label=legends[1], linewidth=2)
my_plots[2], = ax2.plot(rps, [0.0]*11, styles[2], c=cols[2], label=legends[2], linewidth=2)
my_plots[3], = ax2.plot(rps, [0.0]*11, styles[3], c=cols[3], label=legends[3], linewidth=2)
ax1.legend(my_plots[:2], legends[:2], 'upper left')

ax2.legend(my_plots[2:], legends[2:], 'upper right')

#legend([p1], ["Label 1"], loc=1)
#legend([p2], ["Label 2"], loc=4) # this removes l1 from the axes.
#gca().add_artist(l1) # add l1 as a separate artist to the axes

#legend = legend(loc='upper right', shadow=True)
savefig('foo.png',bbox_inches='tight')


