class C(object):
    def __init__(self):
        self._x = 'acb'

    def getx(self):
    	print 'text'
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

a = C()
print a.x

class Class_test(object):
	"""docstring for Class_test"""
	def __init__(self):
		self.value_ = 'arg'
	@property
	def voltage(self):
		print 'i am str'
		return self.value_

b = Class_test()
print b.voltage


