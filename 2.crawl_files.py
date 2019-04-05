# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:42:39 2018

@author: THINKPAD
"""

import pandas as pd
import urllib
import time
import os

path = os.getcwd()[:-4] + '数据与实验结果\\data\\'
fileinfo = pd.read_excel(path + 'fileinfo.xlsx')[0].tolist()
nameinfo = pd.read_excel(path + 'nameinfo.xlsx')[0].tolist()
url = []
end = []
for info in fileinfo:
    date = info[10:20]
    num = info[21:31]
    end.append(info[21:])
    url.append('http://www.cninfo.com.cn/cninfo-new/disclosure/szse/download/'+num+'?announceTime='+date)
# 删去文件名中的空格
count = 0
for name in nameinfo:  
    if ' ' in name:
        nameinfo[count] = name.replace(" ","")
    if '*' in name:
        nameinfo[count] = name.replace("*","")
        #print(name)
    count += 1

filename = []
for i in range(0,len(end)):
    filename.append(nameinfo[i]+end[i])
filenamedf = pd.Series(filename)   
#filenamedf.to_excel('filename.xlsx')

#for iii in range(0,len(filename)-1):
#    if filename[iii+1] == filename[iii]:
#        print (filename[iii])

for n in range(0,len(url)):
    print(url[n])
    print(filename[n])
    
def get_files():
    restcount = 0
    for ii in range(6000,6225):
        url1 = url[ii]
        name = filename[ii]
        urllib.request.urlretrieve(url1, name) 
        restcount += 1
        if restcount % 100 == 0:
            time.sleep(5)
            
#get_files()