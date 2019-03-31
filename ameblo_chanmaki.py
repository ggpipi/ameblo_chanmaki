#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lxml
import requests  # 导入网页请求库
from bs4 import BeautifulSoup  # 导入网页解析库
import time
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

# 开启一个session会话
session = requests.session()

# 设置请求头信息
session.headers = headers

url = r'https://ameblo.jp'

for i in range(1, 10):
    url1 = url+'/kawasemaki/'+'page-'+str(i)+'.html'
    res1 = session.get(url=url1)
    text = res1.content
    soup = BeautifulSoup(text, 'lxml')
    list = soup.find_all('a', class_='skin-titleLink')
    for j in list:
        url2 = url+j['href']
        time.sleep(0.5)
        res2 = session.get(url=url2)
        text = res2.content
        soup = BeautifulSoup(text, 'lxml')
        list1 = soup.find('div', class_='skin-entryBody')
        list1 = list1.find_all('img', src=True)
        #list1 = soup.select('a.detailOn.userImageLink')
        date = soup.find('time')['datetime']
        print(date)
        if len(list1) != 0:
            for k in range(len(list1)):
                url3 = list1[k]['src']
                url3 = url3.replace('?caw=800', '')
                time.sleep(0.5)
                res3 = session.get(url=url3)
                with open('./ameblo_chanmaki/'+date+'-'+str(k)+'.jpg', 'wb') as f:
                    f.write(res3.content)



