class indexer:
	def __getitem__(self,index):
		return index ** 2


X = indexer()
 for x in range(5):
	print X[x]