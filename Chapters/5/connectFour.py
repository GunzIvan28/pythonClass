#!/usr/bin/python
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt']) 

table = [['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'], 
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|']]

def placeMove(playerMove):
	"""Checks board and places move selection."""
	for i in xrange(5,-1,-1):
		if table[i][playerMove[1] - 1] == '|_|':
			table[i][playerMove[1] - 1] = '|' + playerMove[0] + '|'
			return True	
	return False


def player(i):
	"""Changes player and accepts move selection."""
	if (i % 2) == 0:
		print '\nPlayer X.'
		return chooseMove('X')
	else:
		print '\nPlayer O.'
		return chooseMove('O')

def chooseMove(player):
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

# Main
for i in xrange(0, 42):
	clearScreen()
	print '\n%2s%3s%3s%3s%3s%3s%3s' % \
		('1', '2', '3', '4', '5', '6', '7')
	for rowNumber in xrange(6):
		row = ''.join(table[rowNumber])
		print row
	while True:
		if placeMove(player(i)) == False:
			raw_input('Column is full. Press ENTER and choose another move.')
		else:
			break

# Need some way to determine if a column is filled and
# if it is, the player needs to be returned to their move to
# make a new selection.


