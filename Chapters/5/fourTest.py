myList = ['x', 'x', 'x', 'x']
winCheck = ''
for each in myList:
	winCheck += each
	if winCheck == 'xxxx':
		print 'Winner!'
	else:
		print 'Doh!'
