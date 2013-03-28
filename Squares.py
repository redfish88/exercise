class Squares:
	"""docstring for Squares:"""
	def __init__(self, start,stop):
			self.value = start - 1
			self.stop = stop	
	def __iter__(self):
		return self
	def next(self):
		print 'in Next'
		if self.value == self.stop:
			raise StopIteration
		self.value += 1
		return self.value ** 2
x = Squares(1,5)
for i in x:
	print i
print x.value	