#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math
import sys
import re
def font():
    #avoid font problem
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False 

def linear_regression(x, y, quiet=0):
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
    return {'string':string, 'slope':slope, 'intercept':intercept, \
            'r_value':r_value, 'p_value':p_value, 'std_err':std_err,\
            'r_squared':r_squared, 's_slope':s_slope, 's_intercept':s_intercept}
def readdata(filename, need=111):
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
    if need == 111:
        return (data, data_orig, name)
    if need == 110:
        return (data, data_orig)
    if need == 101:
        return (data, name)
    #be aware of the octal!
    if need == 011:
        return (data_orig, name)
    if need == 010:
        return data_orig
    if need == 001:
        return name
    if need == 100:
        return data
    # return (data, data_orig, name)

def readpart(fid, number, need=111):
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
    if need == 111:
        return (data, data_orig, name)
    if need == 110:
        return (data, data_orig)
    if need == 101:
        return (data, name)
    #be aware of the octal!
    if need == 011:
        return (data_orig, name)
    if need == 010:
        return data_orig
    if need == 001:
        return name
    if need == 100:
        return data


def varinfo(data, name):
    print('varable name', name, ':')
    l = len(data)
    print('\tnumber:', l)
    avg = np.mean(data)
    print('\taverage:', avg)
    std1 = math.sqrt(sum((data - avg) ** 2) / (l - 1))
    print('\tstd:', std1)



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


