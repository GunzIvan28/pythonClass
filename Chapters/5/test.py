

table = [['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'], 
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|_|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|X|', '|_|', '|_|', '|_|'],
		['|_|', '|_|', '|_|', '|X|', '|X|', '|_|', '|X|']]

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
allMoveCoordinates = {}
# Loop through tables in table.
for i in xrange((len(table) -1),-1,-1):
	# Loop through the indecies of each table.
	for item in range(len(table[i])):
		# Search for X or O (moves).
		if table[i][item] == '|X|' or table[i][item] == '|O|':
			# If match: append to all moves dictionary.
			allMoveCoordinates.update({item:i})
			print allMoveCoordinates
