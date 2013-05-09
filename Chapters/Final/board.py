from string import uppercase

class board(object):

	def __init__(self):
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

	def displayBoard(self):
		print '%4s%3s%3s%3s%3s%3s%3s%3s%3s%4s' % \
			('1', '2', '3', '4', '5', '6', '7','8','9','10')
		for rowNumber in xrange(10):
			row = uppercase[rowNumber] + ' ' + ''.join(self._board[rowNumber])
			print row


board = board()
board.displayBoard(), board.displayBoard()