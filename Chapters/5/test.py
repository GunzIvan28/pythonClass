

table = [['|O|', '|_|', '|_|', '|X|', '|_|', '|_|', '|_|'], 
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|O|', '|_|', '|_|', '|O|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|X|', '|_|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|X|', '|X|', '|X|', '|X|']]

# x = 0
# for i in xrange((len(table) -1),-1,-1):
# 	coordinateHash = [item for item in range(len(table[i])) if table[i][item] == '|X|']
# 	# Checks for X to the left of another X.
# 	for each in coordinateHash:
# 		if table[i][(each - 1)] == '|_|': 
# 			print 'You found it!'
# 			print each, each - 1

# dict1 = {1 : 1}
# dict2 = {2 : 2}

# dict2.update(dict1)
# print dict2

# def checkRowForMove(i):
# 	for item in range(len(table[i])):
# 		if table[i][item] == '|X|' or table[i][item] == '|O|':
# 			moveCoordinates = {i:item}
# 			return moveCoordinates
# 		else:
# 			return False 

# Init all moves dictionary.
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
		# Splits list item into [0] for row, [1] for move index.
		moveCoordinates = eachSet.split(':')
		moveCoordinates = map(int, moveCoordinates)
		try:
			# Stores X or O based on coordinate return.
			playerMarker = table[moveCoordinates[0]][moveCoordinates[1]]
			winCondition = ''
			for i in xrange(4):
				value = moveCoordinates[1] - i 
				# Checks value for positive index reference and matching move.
				if value >= 0 and table[moveCoordinates[0]][value] == (playerMarker):
					# Creates variable that builds the win condition as it finds it.
					# Win condition is either 'XXXX' or 'OOOO'.
					winCondition += playerMarker[1]
					if winCondition == 'XXXX' or winCondition == 'OOOO':
						print winCondition[0], 'is the winner!'
						break
				# If index reference is less than zero do nothing.
				elif value < 0:
					pass
		except IndexError:
			print 'Invalid index.'

winCheck(getAllMoves())

# Iterating through the coordinates of moves stored in allMoveCoordinates.
# Looking for matching move value three indices away.
# for eachSet in allMoveCoordinates:
# 	# Splits list item into [0] for row, [1] for move index.
# 	moveCoordinates = eachSet.split(':')
# 	moveCoordinates = map(int, moveCoordinates)
# 	try:
# 		# Stores X or O based on coords.
# 		playerMarker = table[moveCoordinates[0]][moveCoordinates[1]]
# 		value = moveCoordinates[1] - 3 
# 		print value
# 		# Checks value for positive index reference and matching move.
# 		if value >= 0 and table[moveCoordinates[0]][value] == (playerMarker):
# 			print 'win!'
# 		# If index reference is less than zero do nothing.
# 		elif value < 0:
# 			print 'less than zero'
# 	except IndexError:
# 		print 'Invalid index.'

# """
# Function: tableParse()
# 	+) Parses table and returns move coordinates in dictionary.
# 		+) Move coordinates are in format:
# 			+) Key:Value = Move:
# """

# """
# Parse entire table:
# 	Store moves (X and O) in dictionary (move:row)
# 		For each pair check:
# 			move - 3 == left
# 			move + 3 == right
# 			row - 3  == up
# 			row + 3  == down
# 			(row - 3) and (move - 3)
# 				== up, left
# 			(row - 3) and (move + 3)
# 				== up, right
# 			(row + 3) and (move - 3)
# 				== down, left
# 			(row + 3) and (move + 3)
# 				== down, right
# 			If the values (X/O) match:
# 				Push in-between values into list:
# 					move - (1/2) == left
# 					move + (1/2) == right
# 					row - (1/2)  == up
# 					row + (1/2)  == down
# 					(row - (1/2)) and (move - (1/2))
# 						== up, left
# 					(row - (1/2)) and (move + (1/2))
# 						== up, right
# 					(row + (1/2)) and (move - (1/2))
# 						== down, left
# 					(row + (1/2)) and (move + (1/2))
# 						== down, right


# """

