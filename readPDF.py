#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 1:50
# @Author  : Kazice
# @Site    : 
# @File    : readPDF.py
# @Software: PyCharm

import pdfminer.pdfparser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# 获得文档对象
fp = open("TestPdf.pdf", "rb")
# 创建一个与文档关联的解释器
parser = pdfminer.pdfparser.PDFParser(fp)

#
doc = pdfminer.pdfparser.PDFDocument()
# 连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 对文档初始化
doc.initialize("")
# 创建PDF资源管理器
resource = PDFResourceManager()
# 参数分析器
laparam = LAParams()
# PDF聚合器
device = PDFPageAggregator(resource, laparams=laparam)
# 创建页面解释器
interpreter = PDFPageInterpreter(resource, device)
#
for page in doc.get_pages():
    # 使用页面解释器
    interpreter.process_page(page)
    # 使用聚合器来获得内容
    layout = device.get_result()
    for out in layout:
        print(out.get_text())

