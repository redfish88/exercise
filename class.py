class Super():
	def method(self):
		print 'in Super.method'

class Sub(Super):
	 def method(self):
	 	print ''
	 	Super.method(self)
	 	print 'ending Sub.method'
x = Super()
x.method()	
x = Sub()
x.method()

