table = [['|O|', '|_|', '|_|', '|X|', '|_|', '|_|', '|_|'], 
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|O|', '|_|', '|_|', '|O|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|X|', '|_|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|X|', '|X|', '|X|', '|X|']]


def getAllMoves():
	allMoveCoordinates = [] 
	# Loop through tables in table.
	for i in xrange((len(table) -1),-1,-1):
		# Loop through the indecies of each table.
		for item in range(len(table[i])):
			# Search for X or O (moves).
			if table[i][item] == '|X|' or table[i][item] == '|O|':
				# If match: append to all moves dictionary.
				# Key:Value = row:move index
				allMoveCoordinates.append(str(i)+':'+str(item))
	return allMoveCoordinates

def winCheck(allMoveCoordinates):
	for eachSet in allMoveCoordinates:
		moveCoordinates = eachSet.split(':')
		moveCoordinates = map(int, moveCoordinates)

		# Checks left.
		try:
			playerMarker = table[moveCoordinates[0]][moveCoordinates[1]]
			winCondition = ''
			for i in xrange(4):
				value = moveCoordinates[1] - i 
				if value >= 0 and table[moveCoordinates[0]][value] == (playerMarker):
					winCondition += playerMarker[1]
						if conditionCheck(winCondition) == playerMarker:
							winner(playerMarker)
				elif value < 0:
					pass
		except IndexError:
			print 'Invalid index.'

		# Checks right.
		try:
			playerMarker = table[moveCoordinates[0]][moveCoordinates[1]]
			winCondition = ''
			for i in xrange(4):
				value = moveCoordinates[1] + i 
				if value >= 0 and table[moveCoordinates[0]][value] == (playerMarker):
					winCondition += playerMarker[1]
						if conditionCheck(winCondition) == playerMarker:
							winner(playerMarker)
				elif value < 0:
					pass
		except IndexError:
			print 'Invalid index.'

		# Check up.
		try:
			playerMarker = table[moveCoordinates[0]][moveCoordinates[1]]
			winCondition = ''
			for i in xrange(4):
				value = moveCoordinates[0] - i 
				if value >= 0 and table[moveCoordinates[0]][value] == (playerMarker):
					winCondition += playerMarker[1]
						if conditionCheck(winCondition) == playerMarker:
							winner(playerMarker)
				elif value < 0:
					pass
		except IndexError:
			print 'Invalid index.'

		# Check down.
		try:
			playerMarker = table[moveCoordinates[0]][moveCoordinates[1]]
			winCondition = ''
			for i in xrange(4):
				value = moveCoordinates[0] + i 
				if value >= 0 and table[moveCoordinates[0]][value] == (playerMarker):
					winCondition += playerMarker[1]
						if conditionCheck(winCondition) == playerMarker:
							winner(playerMarker)
				elif value < 0:
					pass
		except IndexError:
			print 'Invalid index.'

		# Check down.
		try:
			playerMarker = table[moveCoordinates[0]][moveCoordinates[1]]
			winCondition = ''
			for i in xrange(4):
				row = moveCoordinates[0] + i 
				move = moveCoordinates[1] + i
				if row >= 0 and move >= 0 and table[row][move] == (playerMarker):
					winCondition += playerMarker[1]
						if conditionCheck(winCondition) == playerMarker:
							winner(playerMarker)
				elif row < 0 or move < 0:
					pass
		except IndexError:
			print 'Invalid index.'

def conditionCheck(winCondition):
	if winCondition == 'XXXX' or winCondition == 'OOOO':
		return winCondition[0]

def winner(playerMarker):
	print playerMarker, 'wins the game!'
	while True:
		raw_input('Press ENTER to continue.')
		exit()


winCheck(getAllMoves())

"""
Parse entire table:
	Store moves (X and O) in dictionary (move:row)
		For each pair check:
			move - 3 == left
			move + 3 == right
			row - 3  == up
			row + 3  == down
			(row - 3) and (move - 3)
				== up, left
			(row - 3) and (move + 3)
				== up, right
			(row + 3) and (move - 3)
				== down, left
			(row + 3) and (move + 3)
				== down, right
			If the values (X/O) match:
				Push in-between values into list:
					move - (1/2) == left
					move + (1/2) == right
					row - (1/2)  == up
					row + (1/2)  == down
					(row - (1/2)) and (move - (1/2))
						== up, left
					(row - (1/2)) and (move + (1/2))
						== up, right
					(row + (1/2)) and (move - (1/2))
						== down, left
					(row + (1/2)) and (move + (1/2))
						== down, right
"""

