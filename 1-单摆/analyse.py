#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import math

#read data
data = []
data_orig = []
name = []
#order of magnitude
oom = 0
fin = open('./data.txt', 'r')
for i in fin.readlines():
    if i[0] == '#':
        #line start with # is comment
        pass
    elif i[0] == 'e':
        oom = int(i.split()[1])
    elif i[0] == 'n':
        name.append(i.split()[1])
    else:
        data.append(np.array([float(x) * pow(10, oom) for x in i.split()]))
        data_orig.append(np.array([float(x) for x in i.split()]))
        oom = 0
# print(data)

def varinfo(data, name):
    print('varable name', name, ':')
    l = len(data)
    print('number:', l)
    avg = np.mean(data)
    # avg_orig = np.mean(data_orig)
    print('average:', avg)
    # print('average orig:', avg_orig)
    std1 = math.sqrt(sum((data - avg) ** 2) / (l - 1))
    # std1_orig = math.sqrt(sum((data_orig - avg_orig) ** 2) / (l - 1))
    print('std:', std1)
    # print('std orig:', std1_orig)

### main processing ###
for i in range(len(data)):
    varinfo(data[i], name[i])
    varinfo(data_orig[i], name[i] + ' orig')
varinfo(data[1] + .02219, 'real l')
print(data[1] + .02219)
