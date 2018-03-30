#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *
from gendocx import *

font()

fin = open('./data.txt', 'r')

R = readpart(fin, 1)[0][0]
# print(R)

#total 5 main data group
datanum = 5
data = [[] for i in range(datanum)]
for i in range(datanum):
    d, d_o, n = readpart(fin, 3)
    data[i] = [d, d_o]
# print(data)

percent, volt = readpart(fin, 2)

fin.close()



