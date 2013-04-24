#! python
#coding:utf-8

def url():
	url_model = 'http://bi.shequ.10086.cn:58080/MicroStrategy/servlet/mstrWeb?Server=bi-report&Project=139+BI+old&Port=0&evt=4001&src=mstrWeb.4001&visMode=0&reportID=$&reportViewMode=1'
	file_object = open('url.txt')
	for line in file_object:
		line = line.strip('\n')
		print url_model.replace('$',line)
	file_object.close()
if __name__ == '__main__':
	url()