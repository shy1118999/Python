# -*-coding:utf8-*-
# 
from lxml import etree
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>测试常规用法</title>
</head>
<body>
<div class="content">
	<ul id="useful">
		<li>这是第一条信息</li>
		<li>这是第二条信息</li>
		<li>这是第三条信息</li>
	</ul>
	<ul id="useless">
		<li>不需要的信息1</li>
		<li>不需要的信息2</li>
		<li>不需要的信息3</li>
	</ul>
	<div id="url">
	<a href="http://shaohang.xin">少航博客</a>
	<a href="http://hao.shaohang.xin" title="少航博客网址导航">少航博客网址导航</a>
	</div>
</div>
	
</body>
</html>
'''
selector = etree.HTML(html)

# 提取文本
# content = selector.xpath('//ul[@id="useful"]/li/text()')
# content = selector.xpath('//ul/li/text()')
# for each in content:
# 	print(each)

# 提取属性
# link = selector.xpath('//a/@href')
# link = sele .xpath('//div[id="url"]/a/@href')
# for each in link:
# 	print(each)
# 	
title = selector.xpath('//a/@title')
print(title[0])