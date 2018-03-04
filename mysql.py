#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 21:13
# @Author  : Kazice
# @Site    : 
# @File    : mysql.py
# @Software: PyCharm

# 导入开发包
import pymysql.cursors
# 获取链接
connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='wikiurl',
        charset='utf8mb4')
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 查询语句
        sql = "select `urlname`,`urlhref`from`urls`where`id`is not null "
        conut = cursor.execute(sql)
        # print(conut)

        # 查询数据
        result0 = cursor.fetchall()
        result1 = cursor.fetchmany(size=3)
        print(result0)
finally:
    connection.close()


