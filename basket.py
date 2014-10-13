#coding=utf8

basket = []
ask = 'what do you want to put into the basket now:'
#python 2.x
item = raw_input(ask)
#python 3.x
#item = input(ask)
while item != 'nothing':
	basket.append(item)
    #print('Okey')
	print 'Okey'
    #python 2.x
	item = raw_input(ask)
    #python 3.x
    #item = input(ask)
#print('There are %d items in the basket: %s' % (len(basket),basket))
print 'There are %d items in the basket: %s' % (len(basket),basket)
