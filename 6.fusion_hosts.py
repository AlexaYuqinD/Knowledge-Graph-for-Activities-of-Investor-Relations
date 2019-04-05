# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 00:06:57 2018

@author: THINKPAD
"""
import pandas as pd
import numpy as np
import math
import os

path = os.getcwd()[:-4] + '数据与实验结果\\data\\'
hosts = pd.read_excel(path + 'hosts.xlsx')
hostname = hosts['name'].tolist()
code = hosts['companycode'].tolist()
position = hosts['position'].tolist()
#unique = np.unique(name)
def disambi_name(code,name):
    samename = []
    uniquename = []
    uniqueindex = []
    count = -1
    for n in name:
        count += 1
        if n not in uniquename:
            uniquename.append(n)
            uniqueindex.append(count)
        else:
            nameindex = uniquename.index(n)
            nameindex1 = uniqueindex[nameindex]
            samename.append(nameindex1)
            samename.append(count)
    modify1 = []
    modify2 = []
    difpos = []
    for i in range(1,int(len(samename)/2+1)):
        index1 = samename[2*i-2]
        index2 = samename[2*i-1]
        if code[index1] != code[index2]:
            print('same name dif comp')
            modify1.append(index2)
        if position[index1] != position[index2]:
            print('same name dif pos')
            difpos.append(position[index1])
            difpos.append(position[index2])
            modify2.append(index1)
            modify2.append(index2)
#    for m in modify1:
#        name[m] = name[m]+'2'     
    return name,difpos,modify2
hostname,difpos,modify2 = disambi_name(code,hostname)
index3 = modify2[14]
index4 = modify2[15]
position[index4] = position[index3]
uniquename = []
uniqueindex = []
count = -1
for n in hostname:
    count += 1
    if n not in uniquename:
        uniquename.append(n)
        uniqueindex.append(count)
uniquepos = []
for i in uniqueindex:
    uniquepos.append(position[i])
uniquehosts = pd.DataFrame()
uniquehosts['name'] = uniquename
uniquehosts['position'] = uniquepos
uniquehosts.to_excel(path + 'uniquehosts.xlsx')