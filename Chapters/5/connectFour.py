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

def makeMove(playerMove):
	"""Checks board and places move selection."""
	for i in xrange(5,-1,-1):
		if table[i][playerMove[1] - 1] == '|_|':
			table[i][playerMove[1] - 1] = '|' + playerMove[0] + '|'
			break

def player(i):
	"""Changes player and accepts move selection."""
	if (i % 2) == 0:
		print '\nPlayer X.'
		move = raw_input('Choose a number to drop a piece: ')
		playerMove = ['X', int(move)]
		return playerMove
	else:
		print '\nPlayer O.'
		move = raw_input('Choose a number to drop a piece: ')
		playerMove = ['O', int(move)]
		return playerMove

# Main
for i in xrange(0, 42):
	clearScreen()
	print '\n%2s%3s%3s%3s%3s%3s%3s' % \
		('1', '2', '3', '4', '5', '6', '7')
	for rowNumber in xrange(6):
		row = ''.join(table[rowNumber])
		print row
	makeMove(player(i))

"""
if an element is X or O
	check values around it for same value
		if value found

"""