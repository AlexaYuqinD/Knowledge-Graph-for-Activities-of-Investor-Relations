# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:56:58 2018

@author: THINKPAD
"""

from urllib.request import urlopen,Request
from urllib.parse import urlencode
import time, datetime
import re
import os
import pandas as pd
import math

def getstock(page, strdate):
    values = {
        'stock': '',
        'searchkey': '',
        'plate': '',
        # %category_bndbg_szsh半年报告；category_sjdbg_szsh三季度；category_ndbg_szsh年度；category_yjdbg_szsh一季度
        'category': 'category_tzzgx_szsh',
        'trade': '',
        'column': '',
        'columnTitle': '%E5%8E%86%E5%8F%B2%E5%85%AC%E5%91%8A%E6%9F%A5%E8%AF%A2',
        'pageNum': page,
        'pageSize': '50',
        'tabName': 'fulltext',
        'sortName': '',
        'sortType': '',
        'limit': '',
        'seDate': strdate}

    header = urlencode(values).encode('utf8')
    url="http://www.cninfo.com.cn/cninfo-new/announcement/query"
    webRequest=Request(url,header)
    response=urlopen(webRequest)
    re_data=response.read()
    re_data=re_data.decode('utf8')
    #print(re_data)
    dict_data = eval(re_data.replace('null', 'None').replace('true', 'True').replace('false', 'False'))
    print(dict_data)# 转成dict数据，输出看看
    return dict_data
info = []
name = []
title = []
#date2 = time.strftime('%Y-%m-%d', time.localtime())
def get_info(date,info,name):
    page = 1
    totalancm = getstock(str(page),date)['totalAnnouncement']
    totalpage = math.ceil(totalancm/50)
    for page in range(1,totalpage+1):
        #print(page)
        ret = getstock(str(page), date)  
        for items in ret['announcements']:
            if items['announcementTitle'].endswith('投资者关系活动记录表'):       
                if items['adjunctType'] == 'DOCX' or items['adjunctType'] == 'DOC':
                    info.append(items['adjunctUrl'])
                    name.append(items['secName'])
    #                title.append(items['announcementTitle'])   
    return info,name

date1 = '2017-05-01 ~ 2017-12-31'
info,name = get_info(date1,info,name)

#for page in range(1,120):
#    ret = getstock(str(page), date)  
#    for items in ret['announcements']:
#        if items['announcementTitle'].endswith('投资者关系活动记录表'):       
#            if items['adjunctType'] == 'DOCX' or items['adjunctType'] == 'DOC':
#                info.append(items['adjunctUrl'])
#                name.append(items['secName'])
##                title.append(items['announcementTitle'])

date2 = '2017-01-01 ~ 2017-05-01'
info,name = get_info(date2,info,name)

#for page in range(1,44):
#    ret = getstock(str(page), date)    
#    for items in ret['announcements']:
#        if items['announcementTitle'].endswith('投资者关系活动记录表'):       
#            if items['adjunctType'] == 'DOCX' or items['adjunctType'] == 'DOC':
#                info.append(items['adjunctUrl'])
#                name.append(items['secName'])
##                title.append(items['announcementTitle'])
path = os.getcwd()[:-4] + '数据与实验结果\\data\\'

fileinfo = pd.Series(info)
fileinfo.to_excel(path + 'fileinfo.xlsx')
nameinfo = pd.Series(name)
nameinfo.to_excel(path + 'nameinfo.xlsx')

#dateid = []
#for piece in title:
#    dateid.append(piece[:-10])
#
#dateiddf = pd.Series(dateid)
#dateiddf.to_excel('date.xlsx')
