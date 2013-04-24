#coding:utf-8
#99乘法
#通过这个知道了print 默认带一个换行，除非他是以,(逗号)结尾
for x in range(1,10):
	for y in range(1,x+1):
		print '%d*%d=%d\t' % (y,x,x*y),
	print ''

