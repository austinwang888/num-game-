# 產生一個隨機數1-100

import random

r = random.randint(1 ,100)

x = int (input('nubmer 1-100:'))

while x != r :
	if x >= r:
		print ('x > r')
	else :
		print('x< r')
		print(r)
	x = int (input('nubmer 1-100'))
print ('corret')



	


