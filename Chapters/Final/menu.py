from os import system, name
from time import sleep
from string import uppercase

#TESTING:
from players import player
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
		self._shipsAndCoords = {}
		for ship in self._ships:
			while True:
				self._clearScreen()
				self._shipCoords = []
				self._board.display()
				print 'Example placement: A 1 right'
				print 'Place your', ship.title(), '(' + self._ships[ship], 'spaces long' + ')', 'now.'
				self.placementInput = raw_input('--> ')
				checkValue = self._placementCheck(self.placementInput)
				if checkValue == False:
					raw_input('Invalid input. Press ENTER to try again.')
				else:
					self.placementInput = self.placementInput.split(' ')
					if self._board.place(self._ships[ship], self.placementInput) == False:
						raw_input('Invalid placement. Press ENTER to try again.')
					else:
						if self.placementInput[2] == 'right':
							self._shipCoords.append((self.placementInput[0].upper() + self.placementInput[1]))
							for i in xrange(1,int(self._ships[ship])):
								self._shipCoords.append((self.placementInput[0].upper() + str((int(self.placementInput[1]) + i))))
							break
						elif self.placementInput[2] == 'down':
							self._shipCoords.append((self.placementInput[0].upper() + self.placementInput[1]))
							for i in xrange(1,int(self._ships[ship])):
								self._shipCoords.append(chr((ord(self.placementInput[0].upper()) + i)) + (self.placementInput[1]))
							break
			self._shipsAndCoords.update({ship:self._shipCoords})
		return self._shipsAndCoords

	def _placementCheck(self, input):
		input = input.split(' ')
		if len(input) < 3:
			return False
		letterList = []
		for i in xrange(10):
			letterList.append(uppercase[i])
		if input[0].upper() in letterList:
			pass
		else:
			return False
		try:
			if int(input[1]) > 0 and int(input[1]) < 11:
				pass
			else:
				return False
		except ValueError:
			return False
		if input[2].lower() == 'down' or input[2].lower() == 'right':
			pass
		else:
			return False

	# def playInst(self):




player = player()
menu = menu()
menu.intro()
menu.placementInst()
player.storeShips(menu.placeShips(gameboard()))
player.checkHit('A1')