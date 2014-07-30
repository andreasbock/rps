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

legends = ['q_r', 'p_rec', 'p']
cols   = ['green', 'blue', 'purple']
rps    = np.arange(0,1.1,0.1)

#figure()
#subplot(111)

fig, ax1 = subplots()

ax1.set_xlabel('RPS level')
ax1.set_ylabel('Quantities')

ax2 = ax1.twinx()
ax2.set_ylabel('Price')

ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax1.grid(True)

my_plots = [None]*3

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

for idx in [0]:
    my_plots[idx], = ax1.plot(rps, res[idx], c=cols[idx], label=legends[idx], linewidth=2)

for idx in [1,2]:
    my_plots[idx], = ax2.plot(rps, res[idx], c=cols[idx], label=legends[idx], linewidth=2)
    
ax1.legend([my_plots[0]], [legends[0]], 'upper left')
ax2.legend(my_plots[1:], legends[1:], 'upper right')

#legend([p1], ["Label 1"], loc=1)
#legend([p2], ["Label 2"], loc=4) # this removes l1 from the axes.
#gca().add_artist(l1) # add l1 as a separate artist to the axes

#legend = legend(loc='upper right', shadow=True)
savefig('foo.png',bbox_inches='tight')


