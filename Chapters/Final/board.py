from string import uppercase

class gameboard(object):

	def __init__(self):
		self._ships = {'carrier':'5','battleship':'4','cruiser':'3','submarine':'3','destroyer':'2'}
		self._board = [['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|'],
						['|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|','|_|']]
		self._rowKey = {}
		for row in xrange(10):
			self._rowKey.update({str(uppercase[row]):int(row)})

	def display(self):
		print '%4s%3s%3s%3s%3s%3s%3s%3s%3s%4s' % \
			('1', '2', '3', '4', '5', '6', '7','8','9','10')
		for rowNumber in xrange(10):
			row = uppercase[rowNumber] + ' ' + ''.join(self._board[rowNumber])
			print row

	def placeShip(self, length, placeInfo):
		self._board[self._rowKey[placeInfo[0].upper()]][int(placeInfo[1]) - 1] = '|S|'
		if placeInfo[2] == 'right':
			for i in xrange(int(length)):
				while True:
					try:
						self._board[self._rowKey[placeInfo[0].upper()]][(int(placeInfo[1]) - 1) + i] = '|S|'
						break
					except IndexError:
						self._board[self._rowKey[placeInfo[0].upper()]][int(placeInfo[1]) - 1] = '|_|'
						return False
		elif placeInfo[2] == 'down':
			for i in xrange(int(length)):
				while True:
					try:
						self._board[(self._rowKey[placeInfo[0].upper()] + i)][(int(placeInfo[1]) - 1)] = '|S|'
						break
					except IndexError:
						self._board[self._rowKey[placeInfo[0].upper()]][int(placeInfo[1]) - 1] = '|_|'
						return False
		else:
			self._board[self._rowKey[placeInfo[0].upper()]][int(placeInfo[1]) - 1] = '|_|'
			return False

	def placeMarker(self, markerInfo):
		"""markerInfo == [coords, X/O]"""
		self._board[self._rowKey[markerInfo[0].upper()]][int(markerInfo[1]) - 1] = '|' + markerInfo[2] + '|'


