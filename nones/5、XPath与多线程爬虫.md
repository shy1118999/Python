5、XPath与多线程爬虫


XML Path Language：XML路径语言

简介：

	XPath是一门语言
	XPath可以在XML文档中查找信息
	XPath支持HTML
	XPath通过元素和属性进行导航
	XPath可以提取信息
	XPath比正则表达式厉害
	XPath比正则表达式简单

安装XPath
	
	安装lxml库 
	from lxml import etree
	Selector = etree.HTML(网页源代码)
	Selector.xpath(一段神奇的符号)
	
