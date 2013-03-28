cb3 = (lambda color='red': 'turn '+color)
print cb3('blue')
class c(object):
	"""docstring for c"""
 	X = 33
 	def  m(self):
 		X = 44
 		self.X = 55
obj = c()
print obj.X
print c.X 		
obj.m()
print obj.X
class a(c):
   pass

obj1 = a()
print obj1.__class__.__bases__