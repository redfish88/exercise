
#生成器的例子
def addlist(alist):
	for i in alist:
		yield i + 1

alist = [1,2,3,4]

for i in addlist(alist):
	print i

def flatten(nested):
	try:
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested
blist = [[1,2],[3,4,5,6],[6,7],9]
print list(flatten(blist))

