# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 20:04:43 2018

@author: THINKPAD
"""


import pandas as pd
import numpy as np
#import json


event = pd.read_excel('event.xlsx')
#event = event.reset_index(drop=True)
#event.to_excel('event.xlsx')


long = event['companyname'].tolist()
code = event['code'].tolist()
eventid = event['eventid'].tolist()
uniqueid = np.unique(eventid)
#for ids in uniqueid:
#    if len(eventid[eventid == ids]) > 1:
#        print (ids)
simple = []
for ids in eventid:
    simple.append(ids.split('-')[0])

#uniquesimple = np.unique(simple)
#uniquelong = np.unique(long)

uniquelong = []
uniqueindex = []
count = -1
for n in long:
    count += 1
    if n not in uniquelong:
        uniquelong.append(n)
        uniqueindex.append(count)
uniquecode = event['code'][uniqueindex].tolist()
count1 = 0
for codes in uniquecode:
    codes = str(codes)
    if len(codes)<6:
        uniquecode[count1] = 'SZ' + codes.zfill(6)
    else:
        uniquecode[count1] = 'SZ' + codes
    count1 += 1
company_code = pd.DataFrame()
company_code['subject'] = uniquelong
company_code['pred'] = 'code'
company_code['object'] = uniquecode

company_event = event[['companyname','eventid']]
company_event.columns = ['subject','object']
company_event_pred = 'event'
company_event.insert(1,'pred',company_event_pred)

event_type = event[['eventid','eventtype']]
event_type.columns = ['subject','object']
event_type_pred = 'type'
event_type.insert(1,'pred',event_type_pred)
event_place = event[['eventid','place']]
event_place.columns = ['subject','object']
event_place_pred = 'place'
event_place.insert(1,'pred',event_place_pred)
guests = pd.read_excel('newguests.xlsx')
guestr = []
eventr = []
for n in range(0,len(guests)):
    if guests['name'][n] != ' ':
        guestr.append(guests['name'][n])
        eventr.append(guests['eventid'][n])
    else:
        guestr.append(guests['company'][n])
        eventr.append(guests['eventid'][n])
    
event_guest = pd.DataFrame()
event_guest['subject'] = eventr
event_guest['pred'] = 'guest'
event_guest['object'] = guestr  
name = guests['name'].tolist()
uniquename = []
uniqueindex1 = []
count2 = -1
for n in name:
    count2 += 1
    if n == ' ':
        continue
    if n not in uniquename:
        uniquename.append(n)
        uniqueindex1.append(count2)
uniqcompany = guests['company'][uniqueindex1].tolist()
guest_company = pd.DataFrame()
guest_company['subject'] = uniquename
guest_company['pred'] = 'guest_company'
guest_company['object'] = uniqcompany

hosts = pd.read_excel('hosts.xlsx')
event_host = hosts[['eventid','name']]
event_host.columns = ['subject','object']
event_host_pred = 'host'
event_host.insert(1,'pred',event_host_pred)

uniquehosts = pd.read_excel('uniquehosts.xlsx')
pos = uniquehosts['position'].tolist()
count3 = 0
for p in pos:
    if type(p) != str:
        pos[count3] = ' '
    count3 += 1
uniquehosts['position'] = pos
host_position = uniquehosts[uniquehosts['position'] != ' ']
host_position.columns = ['subject','object']
host_position_pred = 'position'
host_position.insert(1,'pred',host_position_pred)

spo = pd.concat([company_code,company_event,event_type,event_place,event_guest,guest_company,event_host,host_position],axis = 0)
spo = spo.reset_index(drop = True)
#spo.to_csv('spo.csv')
