

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
			# Key:Value = moveIndex:Row
			allMoveCoordinates.update({int(item):int(i)})
			print allMoveCoordinates

for move, row in allMoveCoordinates.iteritems():
	# print move, row
	# print table[row], table[row][move]
	try:
		value = move - 9 
		print value
		if table[row][(value)] >= 0 and table[row][(value)] == ('|X|' or '|O|'):
			print 'win!'
		elif value < 0:
			print 'less than zero'
	except IndexError:
		print 'Invalid index.'


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