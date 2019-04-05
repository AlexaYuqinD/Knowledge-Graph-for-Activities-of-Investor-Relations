# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:38:22 2018

@author: THINKPAD
"""
import pandas as pd
import numpy as np
import re
from random import shuffle
import os

path = os.getcwd() + '\\Deep_Learning\\data\\'
path1 = os.getcwd()[:-4] + '数据与实验结果\\data\\'
all_data = path + 'all_data.txt'
data_train = path +'example.train'
data_validate = path + 'example.dev'
data_test = path + 'example.test'


guestlist = pd.read_excel(path1 + 'uniqueguests.xlsx')[0].tolist()
companylist = pd.read_excel(path1 + 'uniquecompany.xlsx')[0].tolist()

guestdata = pd.read_excel(path1 + 'select_guestdata.xlsx')[0].tolist()
guest_for_dl = []
for piece in guestdata:
    spl = re.split(r'-|—|：|:|、|，|,|。|；|/|;|（|）|\s|\u202c',piece)
    while '' in spl:
        spl.remove('')
    for subpiece in spl:
        guest_for_dl.append(subpiece)
g = pd.DataFrame(guest_for_dl)
g.to_excel(path1 + 'guest_for_dl.xlsx')        
  
guest_for_dl = pd.read_excel(path1 + 'guest_for_dl.xlsx')[0].tolist()      

def data_for_model(guest_for_dl):
    with open(file=all_data,
              mode='w',
              encoding='utf-8') as output_file:
        for item in guest_for_dl:                            
            if item in guestlist:
                for n in range(0,len(item)):
                    if n == 0:
                        output_file.write(item[n] + ' B-PER' + '\n') 
                    else:
                        output_file.write(item[n] + ' I-PER' + '\n')                     
            elif item in companylist:
                for n in range(0,len(item)):
                    if n == 0:
                        output_file.write(item[n] + ' B-ORG' + '\n') 
                    else:
                        output_file.write(item[n] + ' I-ORG' + '\n')
            else:
                sign = 0
                for i in range(1,len(item)+1):
                    if item[0:len(item)+1-i] in companylist:
                        sign = 1
                        item1 = item[0:len(item)+1-i]
                        for n in range(0,len(item1)):
                            if n == 0:
                                output_file.write(item1[n] + ' B-ORG' + '\n') 
                            else:
                                output_file.write(item1[n] + ' I-ORG' + '\n')  
                        item2 = item[len(item)+1-i:]   
                        if item2 in guestlist:                                
                            for n in range(0,len(item2)):
                                if n == 0:
                                    output_file.write(item2[n] + ' B-PER' + '\n') 
                                else:
                                    output_file.write(item2[n] + ' I-PER' + '\n')  
                        else:
                            sign1 = 0
                            for k in range(1,len(item2)+1):
                                if item2[0:len(item2)+1-k] in guestlist:
                                    item3 = item2[0:len(item2)+1-k]
                                    for n in range(0,len(item3)):
                                        if n == 0:
                                            output_file.write(item3[n] + ' B-PER' + '\n') 
                                        else:
                                            output_file.write(item3[n] + ' I-PER' + '\n')  
                                    item4 = item2[len(item2)+1-k:]
                                    for n in range(0,len(item4)):
                                        output_file.write(item4[n] + ' O' + '\n')   
                                    sign1 = 1
                                    print('1',item,item2,item4)
                                    break
                            if sign1 == 0:
                                for n in range(0,len(item2)):
                                    output_file.write(item2[n] + ' O' + '\n')   
                                print('2',item,item2)
                        break
                    elif item[0:len(item)+1-i] in guestlist:
                        sign = 1
                        item5 = item[0:len(item)+1-i]
                        for n in range(0,len(item5)):
                            if n == 0:
                                output_file.write(item5[n] + ' B-PER' + '\n') 
                            else:
                                output_file.write(item5[n] + ' I-PER' + '\n')  
                        item6 = item[len(item)+1-i:]
                        for n in range(0,len(item6)):
                            output_file.write(item6[n] + ' O' + '\n')  
                        break
                if sign == 0:
                    for n in range(0,len(item)):
                        output_file.write(item[n] + ' O' + '\n')     
                    print('3',item)          
            output_file.write('\n')
data_for_model(guest_for_dl)

def split_train_validate_test():
    with open(file=all_data,
              mode='r',
              encoding='utf-8') as input_file:
        with open(file=data_train,
                  mode='w',
                  encoding='utf-8') as train_file:
            with open(file=data_validate,
                      mode='w',
                      encoding='utf-8') as validate_file:
                with open(file=data_test,
                      mode='w',
                      encoding='utf-8') as test_file:
                        text = input_file.read().split('\n\n')
                        shuffle(text)
                        for i, line in enumerate(text):
                            #print(i)
                            if i < 180:
                                test_file.write(line + '\n\n')
                            elif i < 360:
                                # word = [x.split('\t')[0] for x in text[i].split('\n')]
                                # word = '\n'.join(word)
                                validate_file.write(line + '\n\n')
                            else:
                                train_file.write(line + '\n\n')
split_train_validate_test()                
