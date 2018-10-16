#coding:utf-8

# 导入re文件
import re

old_url = 'https://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('text.txt','r',encoding='utf-8')
html = f.read()
f.close()

# 抓取标题
# title = re.search('<title>(.*?)</title>',html,re.S).group(1)
# print(title)
# 
# 抓取链接
# links = re.findall('href="(.*?)"',html,re.S)
# for each in links:
# 	print(each)
# 	
# 抓取部分文字，先大后小
# text_fied = re.findall('<ul>(.*?)</ul>',html,re.S)[0]
# the_text = re.findall('">(.*?)</a>',text_fied,re.S)
# for every_text in the_text:
# 	print(every_text)
# sub实现翻页
for i in range(2,total_page+1):
	new_link = re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
	print(new_link)
