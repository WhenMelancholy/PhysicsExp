#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
import math
import sys
import re
def font():
    #avoid font problem
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False 

def linear_regression(x, y, quiet=0, simple=0):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    r_squared = r_value ** 2
    s_slope = slope * math.sqrt((r_value ** -2 - 1) / (len(x) - 2))
    s_intercept = s_slope * math.sqrt(np.mean(x ** 2))
    if quiet == 0:
        print('linear regression:' )
        print('slope:', slope)
        print('intercept:', intercept)
        print('r-value:', r_value)
        print('p-value:', p_value)
        print('std-err:', std_err)
        print('r-squared:', r_squared)
        print('斜率标准差:', s_slope)
        print('截距标准差:', s_intercept)
    string = '''
linear regression: \n \
slope: %g \n \
intercept: %g \n \
r-value: %g \n \
p-value: %g \n \
std-err: %g \n \
r-squared: %g \n \
斜率标准差: %g \n \
截距标准差: %g
''' % (slope, intercept, r_value, p_value, std_err, r_squared, s_slope, s_intercept)
    if simple == 1:
        return slope, intercept
    if simple == 0:
        return {'string':string, 'slope':slope, 'intercept':intercept, \
            'r_value':r_value, 'p_value':p_value, 'std_err':std_err,\
            'r_squared':r_squared, 's_slope':s_slope, 's_intercept':s_intercept}
def readdata(filename, need=0b111):
    data = []; data_orig = []; name = []
    #order of magnitude
    oom = 0
    fin = open(filename, 'r')
    for i in fin.readlines():
        if len(i) == 0:
            continue
        if i[0] == '#':
            #line start with # is comment
            pass
        elif i[0] == 'e':
            oom = int(i.split()[1])
        elif i[0] == 'n':
            #NOTE: may misbehave if some name is not given, 
            #be sure to give all varables name if using this feature
            name.append(i.split()[1])
        else:
            data.append(np.array([float(x) * pow(10, oom) for x in i.split()]))
            data_orig.append(np.array([float(x) for x in i.split()]))
            oom = 0
    if need == 0b111:
        return (data, data_orig, name)
    if need == 0b110:
        return (data, data_orig)
    if need == 0b101:
        return (data, name)
    if need == 0b011:
        return (data_orig, name)
    if need == 0b010:
        return data_orig
    if need == 0b001:
        return name
    if need == 0b100:
        return data
    # return (data, data_orig, name)

def readpart(fid, number, need=0b111):
    #read number line of real data from file descriptor fid
    data = []; data_orig = []; name = []
    cnt = 0
    oom = 0
    while cnt < number:
        i = fid.readline()
        if re.match('^ *\t*\n*$', i):
            #TODO: improve RE
            #if an empty line with no number but blank
            continue
        # print('-->', i)
        if i[0] == '#':
            pass
        elif i[0] == 'e':
            oom = int(i.split()[1])
        elif i[0] == 'n':
            name.append(i.split()[1])
        else:
            data.append(np.array([float(x) * pow(10, oom) for x in i.split()]))
            data_orig.append(np.array([float(x) for x in i.split()]))
            oom = 0
            cnt += 1
    if need == 0b111:
        return (data, data_orig, name)
    if need == 0b110:
        return (data, data_orig)
    if need == 0b101:
        return (data, name)
    if need == 0b011:
        return (data_orig, name)
    if need == 0b010:
        return data_orig
    if need == 0b001:
        return name
    if need == 0b100:
        return data


def varinfo(data, name):
    print('varable name', name, ':')
    l = len(data)
    print('\tnumber:', l)
    avg = np.mean(data)
    print('\taverage:', avg)
    std1 = math.sqrt(sum((data - avg) ** 2) / (l - 1))
    print('\tstd:', std1)

#set x and y limit to make graph better
def setrange(datax, datay):
    mini = min(datay)
    maxi = max(datay)
    plt.ylim(mini - .2 * (maxi - mini), maxi + .2 * (maxi - mini))

def my_sort_by(maj, *sub):
    for i in range(len(maj) - 1):
        for j in range(i, len(maj)):
            if maj[i] > maj[j]:
               maj[i], maj[j] = (maj[j], maj[i]) 
               for k in sub:
                   k[i], k[j] = (k[j], k[i]) 
    return (maj, sub)
if __name__ == '__main__':
    #plot
    plt.scatter(x, y, marker='*', color='black', label='原始数据')
    # plt.plot(x, y, '--', color='green', label='光滑曲线')
    #plt.plot(x, intercept + slope * x, 'r', label='拟合直线')



    plt.xlabel('')
    plt.ylabel('')
    plt.legend(loc=4)
    plt.title('')

    plt.savefig('pic.png')
    plt.show()

    from gendocx import gendocx
    gendocx('gen.docx', 'pic.png', string)


