# -*-coding:utf8-*-
# 
from lxml import etree
html1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div id="test-1">需要的内容1</div>
	<div id="test-2">需要的内容2</div>
	<div id="testfault">需要的内容3</div>
</body>
</html>
'''
html2 = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	<div id="test3">
		我左青龙，
		<span id="tiger">
			右白虎，
			<ul>
				<li>下玄武。</li>
			</ul>
			老牛在当中，
		</span>
		龙头在胸口。
	</div>
</body>
</html>
'''

# selector = etree.HTML(html1)
# content = selector.xpath('//div[starts-with(@id,"test")]/text()')
# for each in content:
# 	print(each)

selector = etree.HTML(html2)
data = selector.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
# print(info)
content_2 = info.replace('\n','').replace(' ','').replace('	','')
print(content_2)
