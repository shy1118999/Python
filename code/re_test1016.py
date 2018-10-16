#coding:utf-8

# 导入re文件
import re

old_url = 'https://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('text.txt','r',encoding='utf-8')
html = f.read()
f.close()

# 抓取标题
title = re.search('<title>(.*?)</title>',html,re.S).group(1)
print(title)