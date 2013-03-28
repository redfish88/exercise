# coding:utf-8
def primeNum():
	a = int(raw_input('please input a num:'))
	for n in range(2,a):
		b = 0

		for x in range(2,n):
			if n % x == 0:
				print n,'equals ',x ,'*',n/x
				b = b + 1
			else:
				if b == 0:
					print n,' is a prime number'


for x in range(10):
	print x
        if  x > 5:
           print x,' 是 大于 5的数'
           break
else:
      print x,'是小于5的数'

for n in range(2, 10):
	for x in range(2, 10):
	         if  x > 0:
	            print 'equals', x, '*'
	            break
	else:
	         # loop fell through without finding a factor
	        print n, 'is a prime number'