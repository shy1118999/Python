#coding:utf-8
#
import requests
import re


class spider:
	def __init__(self):
		print(u'开始爬取内容。。。')

	def getsource(self,url):
		html = requests.get(url)
		return html.text

	def changepage(self,url,total_page):
		now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
		page_group = []
		for i in range(now_page,total_page+1):
			link = re.sub('pageNum=\d+','pageNum=%s'%i,url,re.S)
			page_group.append(link)
		return page_group

	def geteveryclass(self,source):
		everyclass = re.findall('deg="0".*?</li>',source,re.S)
		return everyclass

	def getinfo(self,eachclass):
		info = {}
		info['title'] = re.search('<h2 class="lesson-info-h2"><a href="//www.jikexueyuan.com/course/\d+.html" target="_blank" jktag=".*">(.*?)</a></h2>',eachclass,re.S).group(1)
		info['content'] = re.search('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',eachclass,re.S).group(1)
		timeandlevel = re.findall('<em>(.*?)</em>',eachclass,re.S)
		info['classtime'] = timeandlevel[0]
		info['classlevel'] = timeandlevel[1]
		info['learnnum'] = re.search('<em class="learn-number">(.*?)人学习</em>',eachclass,re.S).group(1)
		return info
	def saveinfo(self,classinfo):
		f = open('info.txt','a',encoding='utf-8')
		for eachclass in classinfo:
			f.writelines('title:'+eachclass['title']+'\n')
			f.writelines('content:'+eachclass['content']+'\n')
			f.writelines('classtime:'+eachclass['classtime']+'\n')
			f.writelines('classlevel:'+eachclass['classlevel']+'\n')
			f.writelines('learnnum:'+eachclass['learnnum']+'\n\n')
		f.close()



if __name__ == '__main__':
	classinfo = []
	url = 'https://www.jikexueyuan.com/course/?pageNum=1'
	jikespider = spider()
	all_links = jikespider.changepage(url,10)
	for link in all_links:
		print(u'正在处理页面：'+link)
		html = jikespider.getsource(link)
		everyclass = jikespider.geteveryclass(html)
		# print(everyclass)
		for each in everyclass:
			info = jikespider.getinfo(each)
			# print(info)
			classinfo.append(info)
	# print(classinfo)
	jikespider.saveinfo(classinfo)
