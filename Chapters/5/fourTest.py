from time import clock

table = [['|O|', '|_|', '|_|', '|X|', '|X|', '|O|', '|_|'], 
		['|_|', '|_|', '|X|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|X|', '|X|', '|O|', '|_|', '|O|', '|_|'],
		['|_|', '|_|', '|O|', '|_|', '|_|', '|_|', '|_|'],
		['|X|', '|_|', '|_|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|O|', '|X|', '|X|', '|X|']]

def winCheck(moves):
	"""Parses argument for winning strings. """
	if 'XXXX' in moves:
		return 'X'
	elif 'OOOO' in moves:
		return 'O'
	else:
		return False

# Parameters are the starting x and y of the diagonal. 
def diagCheck(x=0, y=3, loop=4, counter=0):
	"""Checks the ranges of diagonals that support possible win conditions."""
	moves = ''
	for i in xrange(loop):
		if i == 0:
			moves +=table[y][x][1]
			print x, y, counter
		else:
			if counter < 6:
				x += 1
				y -= 1
			else:
				x += 1
				y += 1
			print x, y, counter
			moves += table[y][x][1]
	print '---'
	winner = winCheck(moves)
	if winner == False:
		"""Holy mother of recursion, Batman."""
		counter += 1
		if counter == 1:
			"""Starts upper right to bottom left diagonals."""
			diagCheck(0, 4, 5, counter)
		elif counter == 2:
			diagCheck(0, 5, 6, counter)
		elif counter == 3: 
			diagCheck(1, 5, 6, counter)
		elif counter == 4:
			diagCheck(2, 5, 5, counter)
		elif counter == 5:
			diagCheck(3, 5, 4, counter)
		elif counter == 6:
			"""Starts top left to bottom right diagonals."""
			diagCheck(0, 2, 4, counter)	
		elif counter == 7:
			diagCheck(0, 1, 5, counter)	
		elif counter == 8:
			diagCheck(0, 0, 6, counter)
		elif counter == 9:
			diagCheck(1, 0, 6, counter)
		elif counter == 10:
			diagCheck(2, 0, 5, counter)
		elif counter == 11:
			diagCheck(3, 0, 4, counter)
	else:
		print winner

clock()
diagCheck()
print clock()

# Checks for wins in a column. 
for x in xrange(7):
	columnMoves = ''
	for y in xrange(6):
		columnMoves += table[y][x][1]
	winCheck(columnMoves)

# Checks for wins in a row.
for y in xrange(6):
	rowMoves = ''
	for x in xrange(7):
		rowMoves += table[y][x][1]
	winCheck(rowMoves)


