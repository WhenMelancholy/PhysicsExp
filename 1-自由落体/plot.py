#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

#avoid font problem
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 

#read data
data = []
#order of magnitude
oom = 0
fin = open('./data.txt', 'r')
for i in fin.readlines():
    if i[0] == '#':
        #line start with # is comment
        pass
    elif i[0] == 'e':
        oom = int(i.split()[1])
    else:
        data.append(np.array([float(x) * pow(10, oom) for x in i.split()]))
        oom = 0
# print(data)

### main processing ###
l = len(data[0])
x = data[1]
y0 = data[0]
data.append(y0 / x)
y1 = data[2]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y1)
# z = np.polyfit(x, y1, 1)
s_slope = slope * math.sqrt((r_value ** -2 - 1) / (l - 2))
s_intercept = s_slope * math.sqrt(np.mean(x ** 2))
print('linear regression:' )
print('slope:', slope)
print('intercept:', intercept)
print('r-value:', r_value)
print('p-value:', p_value)
print('std-err:', std_err)
print('r-squared:', r_value ** 2)
print('斜率标准差:', s_slope)
print('截距标准差:', s_intercept)



print('算得重力加速度:', 2 * slope)

#plot
plt.scatter(x, y1, marker='*', color='black', label='原始数据')
# plt.plot(x, y1, '--', color='green', label='光滑曲线')
plt.plot(x, intercept + slope * x, 'r', label='拟合直线')

plt.xlabel('时间 t/s')
plt.ylabel('平均速度 H/t / m/s')
plt.legend(loc=4)
plt.title('小球下落平均速度与时间关系图')

plt.savefig('pic.png')
plt.show()

