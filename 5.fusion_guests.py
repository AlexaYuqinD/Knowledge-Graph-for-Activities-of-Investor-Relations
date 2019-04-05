# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 19:07:19 2018

@author: THINKPAD
"""

import pandas as pd
import numpy as np
import json
import os

#event = pd.read_excel('event.xlsx')
#event = event.reset_index(drop=True)
#event.to_excel('event.xlsx')

#companies = event['companyname'].tolist()
#company_list = np.unique(companies)
#codes = event['code'].tolist()
#codes_list = np.unique(codes)
#companylist = pd.DataFrame(company_list)
#companylist.to_excel('companylist.xlsx')

path = os.getcwd()[:-4] + '数据与实验结果\\data\\'
guests = pd.read_excel(path + 'guests.xlsx')
guestcompany = guests['company'].tolist()
file1 = path + 'list.json'
with open(file=file1, mode='r', encoding='utf-8') as file:
    cities = json.load(file)
realcity = []
for city in cities.keys():
    if city.endswith('00'):
        realcity.append(cities[city])
        
def resolution_company(guestcompany,realcity):
    uniquecompany = np.unique(guestcompany)
    newcompany = []
    for company in guestcompany:
        if len(company) > 4:
            start = company[0:2]
            test1 = start+'省'
            test2 = start+'市'
            if test1 in realcity or test2 in realcity:
                company1 = company[2:]
                if company1 in uniquecompany:
                    newcompany.append(company1)
                    continue
                elif len(company1)>3:
                    mark = 0
                    for s in range(0,len(company)-1):
                        for k in range(1,len(company)):
                            if company[s:k] in uniquecompany and mark == 0:
                                newcompany.append(company[s:k])
                                print(company,'...',company[s:k])
                                mark = 1
                                break                    
                            if s == len(company)-2 and k == len(company)-1 and mark == 0:
                                newcompany.append(company)
                                #print('1111')
                else:
                    newcompany.append(company)
                    #print('2222')
            else:
                mark1 = 0
                for s in range(0,len(company)-1):
                    for k in range(1,len(company)):
                        if company[s:k] in uniquecompany and mark1 == 0:
                            newcompany.append(company[s:k])
                            print(company,'...',company[s:k])
                            mark1 = 1
                            break                    
                        if s == len(company)-2 and k == len(company)-1 and mark1 == 0:
                            newcompany.append(company)
                            #print('3333')
        else:
            newcompany.append(company)
            #print('4444')
    return newcompany

newcompany = resolution_company(guestcompany,realcity)
guests['company'] = newcompany
guestname = guests['name'].tolist()

def disambi_guests_name(newcompany,name):
    samename = []
    uniquename = []
    uniqueindex = []
    count = -1
    for n in name:
        count += 1
        if n == ' ':
            continue
        if n not in uniquename:
            uniquename.append(n)
            uniqueindex.append(count)
        else:
            nameindex = uniquename.index(n)
            nameindex1 = uniqueindex[nameindex]
            samename.append(nameindex1)
            samename.append(count)
    modify = []
    for i in range(1,int(len(samename)/2+1)):
        index1 = samename[2*i-2]
        index2 = samename[2*i-1]
        if newcompany[index1] != newcompany[index2]:
            print('same name dif comp')
            modify.append(index2)
    for m in modify:
        name[m] = name[m]+'2'       
    return name

newname = disambi_guests_name(newcompany,guestname)
guests['name'] = newname

guests = guests.reset_index(drop = True)
guests.to_excel(path + 'newguests.xlsx')
        
        

                         
        