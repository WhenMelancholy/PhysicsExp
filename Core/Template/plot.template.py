#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from template import *
from gendocx import *

font()

#read
# data, data_orig, name = readdata('./data.txt', need=0b111)
# fin = open('./data.txt', 'r')
# fin.close()

#data process


#linear regression and plot
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

#generate docx #1
# gendocx('gen.docx', 'pic.png', result['string'])

#generate docx #2
# docu = Document()
# docuaddtitle(docu)
# docuappend(docu, './picfull.png', './figure_1.png', './pic.png', result['string'], './picx.png')
# docu.save('gen.docx')


