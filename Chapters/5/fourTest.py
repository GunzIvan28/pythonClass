# myList = ['x', 'x', 'x', 'x']
# winCheck = ''
# for each in myList:
# 	winCheck += each
# 	if winCheck == 'xxxx':
# 		print 'Winner!'
# 	else:
# 		print 'Doh!'


table = [['|O|', '|_|', '|_|', '|X|', '|X|', '|_|', '|_|'], 
		['|_|', '|_|', '|X|', '|X|', '|O|', '|_|', '|_|'],
		['|_|', '|X|', '|X|', '|O|', '|_|', '|O|', '|_|'],
		['|_|', '|_|', '|O|', '|_|', '|_|', '|_|', '|_|'],
		['|x|', '|O|', '|_|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|O|', '|X|', '|X|', '|X|']]



# Paramters are the starting x and y of the diagonal. 
# def diagCheck(x, y, counter):
# 	moves = ''
# 	for i in xrange((y + 1)):
# 		if i == 0:
# 			moves += table[y][i][1]
# 		else:
# 			y -= 1
# 			x += 1
# 			moves += table[y][x][1]
# 	winner = winCheck(moves)
# 	if winner == False:
# 		"""Holy mother of recursion, Batman."""
# 		counter += 1
# 		if counter == 1:
# 			diagCheck(0, 4, counter)
# 		elif counter == 2:
# 			diagCheck(0, 5, counter)
# 		elif counter == 3: 
# 			diagCheck(1, 6, counter)
# 	elif counter == 6:
# 		return False

def winCheck(moves):
	if 'XXXX' in moves:
		print 'X'
	elif 'OOOO' in moves:
		print 'O'
	else:
		return False

# diagCheck(0, 3, 0)


columnMoves = ''
for x in xrange(7):
	for y in xrange(6):
		columnMoves += table[y][x][1]
	winCheck(columnMoves)

rowMoves = ''
for y in xrange(6):
	for x in xrange(7):
		rowMoves += table[y][x][1]
	winCheck(rowMoves)
	

# x = 7
# y = 6
# diagMoves = ''

# for row in xrange(x):
# 	if x > 3:
# 		pass
# 	else:
# 		for column in xrange(y, -1, -1):
# 			if y > 3:
# 				pass
# 			else:
# 				diagMoves += table[row][column][1]
# print 'diagMoves:', diagMoves



