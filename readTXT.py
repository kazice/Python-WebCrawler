#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 0:25
# @Author  : Kazice
# @Site    : 
# @File    : readTXT.py
# @Software: PyCharm

from urllib.request import urlopen

html = urlopen("https://en.wikipedia.org/robots.txt")
print(html.read().decode("utf-8"))