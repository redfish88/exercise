def sort1(array):
	for i in range(len(array)-1,0,-1):
		for j in range(0,i):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]

if __name__ == '__main__':
	a = [123,343,55,2]
	sort1(a)
	print a
