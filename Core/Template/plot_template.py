#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/home/petergu/PhysicsExp/Core'))

from Core.mainfunc import *
from Core.gendocx import *

font()

#read data
# #1
# data, data_orig, name = readdata('./data.txt', need=0b111)
# #2
# fin = open('./data.txt', 'r')
# x = readoneline(fin)
# y = readoneline(fin)
# z = readonenumber(fin)
# fin.close()

#data process


#linear regression and plot
# #1
# result = linear_regression(x, y)
# setrange(x, y)
# plt.scatter(x, y, marker='o', color='black', label='原始数据')
# plt.plot(x, result['intercept'] + result['slope'] * x, 'r', label='拟合直线')
# plt.xlabel('')
# plt.ylabel('')
# plt.legend(loc=4)
# plt.title('')
# plt.savefig('pic.png')
# plt.show()

# #2
#use automate tool
# simple_linear_plot(x, y, xlab='x axis', ylab='y axis', title='my pic', save='pic.png')


#generate docx #1
# gendocx('gen.docx', 'pic.png', result['string'])

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


