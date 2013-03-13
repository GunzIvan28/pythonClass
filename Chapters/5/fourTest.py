# myList = ['x', 'x', 'x', 'x']
# winCheck = ''
# for each in myList:
# 	winCheck += each
# 	if winCheck == 'xxxx':
# 		print 'Winner!'
# 	else:
# 		print 'Doh!'


table = [['|O|', '|_|', '|_|', '|X|', '|X|', '|_|', '|_|'], 
		['|_|', '|_|', '|X|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|X|', '|X|', '|_|', '|_|', '|O|', '|_|'],
		['|_|', '|X|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|x|', '|X|', '|_|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|X|', '|X|', '|X|', '|X|']]

def diagCheck(x, y, counter):
	moves = ''
	for i in xrange((y + 1)):
		if i == 0:
			moves += table[y][i][1]
		else:
			y -= 1
			x += 1
			moves += table[y][x][1]
	winner = conditionCheck(moves)
	if winner == False:
		"""Holy mother of recursion, Batman."""
		counter += 1
		if counter == 1:
			diagCheck(0, 4, counter)
		elif counter == 2:
			diagCheck(0, 5, counter)
		elif counter == 3: 
			diagCheck(1, 6, counter)
	elif counter == 6:
		return False



def conditionCheck(moves):
	if 'XXXX' in moves:
		print 'X'
	elif 'OOOO' in moves:
		return 'O'
	else:
		return False

diagCheck(0, 3, 0)


# columnMoves = ''
# for x in xrange(7):
# 	for y in xrange(6):
# 		columnMoves += table[y][x][1]
# print columnMoves

# rowMoves = ''
# for y in xrange(6):
# 	for x in xrange(7):
# 		rowMoves += table[y][x][1]
	# if 'XXXX' in rowMoves:
	# 	print 'Winner!'
# print rowMoves

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



