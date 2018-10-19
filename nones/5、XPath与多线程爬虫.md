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

XPath与HTML结构

	树桩结构
	逐层展开
	逐层定位
	寻找独立节点

获取网页元素的Xpath

	手动分析法
	Chrome生成法


应用XPath提取内容

	//定位根节点
	/往下层寻找
	提取文本内容:/text()
	提取属性内容:/@xxxx
	
神器XPath的特殊用法

	以相同的字符开头

		starts-with(@属性名称，属性字符相同部分)

	标签套标签

		string(.)

Python的并行化

	多个线程同时处理任务
	高效
	快速

map的使用

	map函数一手包办了序列操作、参数传递和结果保存等一系列的操作。
	from multiprocessing.dummy import Pool
	pool = Pool(4)
	results = pool.map(爬取函数，网址列表)
	