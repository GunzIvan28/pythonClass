from os import system, name
from time import sleep

#TESTING:
from board import gameboard

class menu(object):

	def __init__(self):
		self._ships = {'carrier':'5','battleship':'4','cruiser':'3','submarine':'3','destroyer':'2'}

	def _clearScreen(self): 
		system(['clear','cls'][name == 'nt'])

	def intro(self):
		self._clearScreen()
		print '\n\tWelcome to Battleship!'
		sleep(2)

	def placementInst(self):
		self._clearScreen()
		print 'INSTRUCTIONS:'
		print '\nTime to prepare your fleet!'
		print '\nShips can only be placed in vertical or horizontal directions.'
		print '\nBegin by choosing the coordinate where you would like your ship'
		print 'to begin. Then choose a direction. Directions can only be down or'
		print 'right.'
		print '\nYou will have 5 ships to position.\n'
		raw_input('Press ENTER to continue.')

	def placeShips(self, preGameBoard):
		self._clearScreen()
		self._board = preGameBoard
		for ship in self._ships:
			while True:
				self._board.display()
				print 'Example placement: A 1 right'
				print 'Place your', ship.title(), '(' + self._ships[ship], 'spaces long' + ')', 'now.'
				self.placementInput = raw_input('--> ')
				if self._board.place(self._ships[ship], self.placementInput) == False:
					raw_input('Invalid placement. Press ENTER to try again.')
				else:
					break
				# checkValue = self._placementCheck(self.placementInput)
				# if checkValue == False:

	def placementCheck(self, input):
		input = input.split(' ')
		for i in xrange(10):
			letterList.append(uppercase[i])
		if input[0].upper() in letterList:
			return True
		else:
			return False
		try:
			if int(input[1]) > -1 and input[1] < 11:
				return True
			else:
				return False
		except ValueError:
			return False
		if input[2].lower() == 'down' or input[2].lower() == 'right':
			return True
		else:
			return False




menu = menu()
menu.intro()
menu.placementInst()
menu.placeShips(gameboard())