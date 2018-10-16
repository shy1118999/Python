#coding:utf-8
#
import requests
import re

# html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')
# print(html.text)
# 
# 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3528.4 Safari/537.36'}
# html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers = headers)
html.encoding = 'utf-8'
# print(html.text)
title = re.findall('color:#666666;">(.*?)</span>',html.text,re.S)
for each in title:
	print(each)
chinese = re.findall('color: #039;">(.*?)</a>',html.text,re.S)
for each in chinese:
	print(each)
