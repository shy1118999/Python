#coding:utf-8
import re

secret_code = 'asfdsl5ksagxxIxxasfeivaa452xxlovexxas54vedaxxyouxxaf4ea'
# .的使用
# a = 'xy123'
# b = re.findall('x..', a)
# print(b)

# *的使用
# a = 'xxyxy12'
# b = re.findall('x*',a)
# print b

# ?的使用
# a = 'xy123'
# b = re.findall('x?',a)
# print(b)

# .*与.*?的使用
# b = re.findall('xx.*xx',secret_code)
# print(b)
#
# c = re.findall('xx.*?xx',secret_code)
# print(c)
#
# d = re.findall('xx(.*?)xx',secret_code)
# print(d)
# for each in d:
#     print(each)

# 有换行的时候
# s = '''sdaxxhello
# xxasfhajsxxwordxxask'''
#
# d = re.findall('xx(.*?)xx',s,re.S)
# print(d)

# 对比findall与search的区域
# s2 = 'asdfxxIxx123xxlovexxafasdfxxIxx123xxlovexxaf'
# f = re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
# print(f)
# #
# f2 = re.findall('xx(.*?)xx123xx(.*?)xx',s2)
# print(f2[0][1])

# sub的使用
# s = 'sad123asfsa123as'
# output = re.sub('123(.*?)123', '123%d123' % 789, s)
# print(output)
