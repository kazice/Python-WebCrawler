#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 23:31
# @Author  : Kazice
# @Site    : 
# @File    : taobaoItem.py
# @Software: PyCharm

# 引入开发包
import urllib.request
# import requests
# from bs4 import BeautifulSoup
import re
import pymysql.cursors


# 打开网页，获取网页内容
def url_open(url):
    headers = ("user-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return data


# 将数据存入mysql中
def data_import(sql, param):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='laptoptb',
                                 charset='utf8mb4')
    try:
        # 获取会话指针
        with connection.cursor() as cursor:
            # 执行SQL语句
            cursor.execute(sql, param)
            # 提交
            connection.commit()
    finally:
        connection.close()


url1 = "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q="
url2 = "&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&p4ppushleft=5%2C48&s="
keywd = "笔记本电脑"
keywords = urllib.request.quote(keywd)
number = 10
try:
    for k in range(0, number):
        url = url1+keywords+url2+str(k*48)
        resp = url_open(url)
        # 定义各个字段正则匹配规则
        img_pat = '"pic_url":"(//.*?)"'
        name_pat = '"title":"(.*?)"'
        price_pat = '"price":"(.*?)"'
        sales_pat = '"month_sales":"(.*?)"'
        # 查找满足匹配规则的内容，并存在列表中
        imgL = re.compile(img_pat).findall(resp)
        nameL = re.compile(name_pat).findall(resp)
        priceL = re.compile(price_pat).findall(resp)
        salesL = re.compile(sales_pat).findall(resp)
        for j in range(len(imgL)):
            # 商品图片链接
            img = "http:"+imgL[j]
            # 商品名称
            name = nameL[j]
            # 商品价格
            price = priceL[j]
            # 商品付款人数
            sales = salesL[j]
            print('正在爬取第'+str(k)+'页第'+str(j)+'个商品信息...')
            sqlcmd = "insert into `notecomp`(`name`,`price`,`sales`,`img`)values(%s,%s,%s,%s)"
            params = (name, price, sales, img)
            data_import(sqlcmd, params)
            print("爬取完成，且数据已存入数据库")
except Exception as e:
    print(str(e))
# print("任务完成")


