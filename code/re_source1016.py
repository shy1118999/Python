#coding:utf-8
#
import re
import requests

# 读取源代码文件
f = open('source.html','r',encoding='utf-8')
html = f.read()
f.close()

# 匹配图片属性
zhiye_div = re.findall('<div class="zhiye">(.*?)</div>',html,re.S)[0]

pic_url = re.findall('<img src="(.*?)"',zhiye_div,re.S)
i =0
for each in pic_url:
	print('now downloading:'+each)
	pic = requests.get(each)
	fp = open('pic\\'+str(i)+'.png','wb')
	fp.write(pic.content)
	fp.close()
	i +=1


