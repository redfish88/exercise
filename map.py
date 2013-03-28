# coding:utf-8
# map函数的使用
# 输出目录下 指定后缀的文件名

import os


def filterFile(floder,ext):
	for filename in os.listdir(floder):
		if os.path.isdir(floder + '/' + filename):
			filterFile(floder + '/' + filename,ext)
		elif True in map(filename.endswith,ext):
			print filename
ext = ['.py']
filterFile('E:\pydemo',ext)

