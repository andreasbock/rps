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

legends = ['q_r', 'q_n', 'p_rec', 'p']
cols   = ['green', 'red', 'blue', 'purple']
rps    = np.arange(0,1.1,0.1)

figure()
grid(True)
subplot(111)
ylabel('Quantities')

idx = 0
for line in lines:
    if line and line.startswith("i") and line[1].isdigit():
        res = parse_result(line.split())
        #print res
        plot(rps, res, c=cols[idx], label=legends[idx], linewidth=2)
        idx += 1
legend = legend(loc='upper right', shadow=True)
xlabel('RPS level')
savefig('foo.png',bbox_inches='tight')
