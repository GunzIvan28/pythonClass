#!/usr/bin/python
"""
Program: Connect Four
Author: Bill Minear

Notes:
	+) Not very reader friendly.
	+) Could benefit from separating functions
		into a separate file for importing.

"""
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt']) 

# Game board.
table = [['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'], 
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|']]

def player(i):
	"""Alternates player, uses chooseMove to return a move selection."""
	if (i % 2) == 0:
		print '\nPlayer X.'
		return chooseMove('X')
	else:
		print '\nPlayer O.'
		return chooseMove('O')

def chooseMove(player):
	"""Asks for and returns move selection."""
	while True:
		move = raw_input('Choose a number to drop a piece: ')
		try:
			if int(move) < 1 or int(move) > 7:
				print '\nChoose a number from 1 to 7.'
				raw_input('Press ENTER to try again.')
			else:
				playerMove = [player, int(move)]
				return playerMove
		except ValueError:
			print '\nInvalid input. Please choose a number from 1 to 7.'
			raw_input('Press ENTER to try again.')

def placeMove(playerMove):
	"""Checks board and places move."""
	for row in xrange(5,-1,-1):
		if table[row][playerMove[1] - 1] == '|_|':
			table[row][playerMove[1] - 1] = '|' + playerMove[0] + '|'
			return True	
	return False

def rowColumnCheck():
	"""Checks rows and columns for a win."""
	# Checks for wins in a column.
	for x in xrange(7):
		columnMoves = ''
		for y in xrange(6):
			columnMoves += table[y][x][1]
		columnWin = winCheck(columnMoves)
		if columnWin != False:
			return columnWin

	# Checks for wins in a row.
	for y in xrange(6):
		rowMoves = ''
		for x in xrange(7):
			rowMoves += table[y][x][1]
		rowWin = winCheck(rowMoves)
		if rowWin != False:
			return rowWin
	return False

def diagCheck(x=0, y=3, loop=4, counter=0):
	"""Checks the ranges of diagonals that support possible win conditions.
		This might be the ugliest thing I've ever written. Recursion is weird."""
	moves = ''
	for i in xrange(loop):
		if i == 0:
			moves +=table[y][x][1]
		else:
			if counter < 6:
				x += 1
				y -= 1
			else:
				x += 1
				y += 1
			moves += table[y][x][1]
	winner = winCheck(moves)
	if winner == False:
		"""Holy mother of recursion, Batman."""
		counter += 1
		if counter == 1:
			"""Starts top right to bottom left diagonals."""
			return diagCheck(0, 4, 5, counter)
		elif counter == 2:
			return diagCheck(0, 5, 6, counter)
		elif counter == 3: 
			return diagCheck(1, 5, 6, counter)
		elif counter == 4:
			return diagCheck(2, 5, 5, counter)
		elif counter == 5:
			return diagCheck(3, 5, 4, counter)
		elif counter == 6:
			"""Starts top left to bottom right diagonals."""
			return diagCheck(0, 2, 4, counter)	
		elif counter == 7:
			return diagCheck(0, 1, 5, counter)	
		elif counter == 8:
			return diagCheck(0, 0, 6, counter)
		elif counter == 9:
			return diagCheck(1, 0, 6, counter)
		elif counter == 10:
			return diagCheck(2, 0, 5, counter)
		elif counter == 11:
			return diagCheck(3, 0, 4, counter)
		elif counter == 12:
			return winner 
	else:
		return winner

def winCheck(moves):
	"""Parses argument for winning strings."""
	if 'XXXX' in moves:
		return 'X'
	elif 'OOOO' in moves:
		return 'O'
	else:
		return False

# Main loop
def main():
	"""Program flow control."""
	for i in xrange(0, 42):	# 42 for the number of moves on the board.
		clearScreen()
		# Printing the board.
		print '\n%2s%3s%3s%3s%3s%3s%3s' % \
			('1', '2', '3', '4', '5', '6', '7')
		for rowNumber in xrange(6):
			row = ''.join(table[rowNumber])
			print row
		# Win checking, move checking, and move making.
		while True:
			if i > 6:
				rowColumnWinner = rowColumnCheck()
				if rowColumnWinner != False:
					print '\nThe winner is:', rowColumnWinner + '!'
					raw_input('Press ENTER to exit the game.')
					exit()
				diagWinner = diagCheck()
				if diagWinner != False:
					print '\nThe winner is:', diagWinner + '!'
					raw_input('Press ENTER to exit the game.')
					exit()
			if placeMove(player(i)) == False:
				raw_input('Column is full. Press ENTER and choose another move.')
			else:
				break
		if i == 41:
			print 'The game is a draw!'
			raw_input('Press ENTER to exit the game.')
			exit()

main()