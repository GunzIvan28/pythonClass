"""
Program: Battleship
Module: menus
Author: Bill Minear
"""
from os import system, name
from time import sleep
from string import uppercase

class menu(object):
	"""Drives most of the interaction in the game."""

	def __init__(self):
		self._ships = {'carrier':'5','battleship':'4','cruiser':'3','submarine':'3','destroyer':'2'}

	def _clearScreen(self): 
		system(['clear','cls'][name == 'nt'])

	def intro(self):
		"""Welcomes you to the game."""
		self._clearScreen()
		print '\n\tWelcome to Battleship!'
		sleep(2)

	def placementInst(self):
		"""Fleet placement instructions."""
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
		"""Fleet placement interaction."""
		self._clearScreen()
		self._board = preGameBoard
		self._shipsAndCoords = {}
		for ship in self._ships:
			while True:
				self._clearScreen()
				self._shipCoords = []
				self._board.display()
				print '(Example placement: A 1 right or A 1 down)'
				print 'Place your', ship.title(), '(' + self._ships[ship], 'spaces long' + ')', 'now.'
				self.placementInput = raw_input('--> ')
				checkValue = self._placementCheck(self.placementInput)
				if checkValue == False:
					raw_input('Invalid input. Press ENTER to try again.')
				else:
					self.placementInput = self.placementInput.split(' ')
					if self._board.placeShip(self._ships[ship], self.placementInput) == False:
						raw_input('Invalid placement. Press ENTER to try again.')
					else:
						if self.placementInput[2].lower() == 'right':
							self._shipCoords.append((self.placementInput[0].upper() + self.placementInput[1]))
							for i in xrange(1,int(self._ships[ship])):
								self._shipCoords.append((self.placementInput[0].upper() + str((int(self.placementInput[1]) + i))))
							break
						elif self.placementInput[2].lower() == 'down':
							self._shipCoords.append((self.placementInput[0].upper() + self.placementInput[1]))
							for i in xrange(1,int(self._ships[ship])):
								self._shipCoords.append(chr((ord(self.placementInput[0].upper()) + i)) + (self.placementInput[1]))
							break
			self._shipsAndCoords.update({ship:self._shipCoords})
		raw_input('All ships are ready. Press ENTER to continue.')
		return self._shipsAndCoords

	def _placementCheck(self, input):
		"""Poorly hacked together means of determining if fleet placement
			input is valid."""
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

	def mainInst(self):
		"""Worst description of how to play Battleship ever."""
		self._clearScreen()
		print 'INSTRUCTIONS:'
		print '\nTime for battle!'
		print "\nThe objective is to sink the computer's ships by attacking"
		print "the coordinates where they are positioned."
		print "\nWhen it's your turn, input attack coordinates as so:"
		print '\n A1'
		print '\nIf the attack hits, the board will display an X. If it'
		print 'misses, the board will display an O.'
		raw_input('\nPress ENTER to continue.')

	def mainGame(self, human, computer, humanBoard, hitBoard):
		"""Focal point of the game - attacking eachother."""
		while True:
			while True:
				"""Human move."""
				if computer.checkWin() == True:
					raw_input('\nYou win! Press ENTER to exit.')
					exit()
				else:
					self._clearScreen()
					hitBoard.display()
					print 'X = Hit; O = Miss'
					humanMove = raw_input('Your move: ')
					if self._validAttackCheck(humanMove) == False:
						raw_input("Invalid input. Press ENTER to try again.")
					else:
						if human.checkAttacks(humanMove) == False:
							raw_input("You've already attacked there! Press ENTER to try again.")
						else:
							humanMove = computer.checkHit(humanMove.upper())
							human.addToAttacks(humanMove[0] + humanMove[1])
							hitBoard.placeMarker(humanMove)
							self._clearScreen()
							hitBoard.display()
							raw_input('Press ENTER to continue.')
							break
			while True:
				"""Computer move."""
				if human.checkWin():
					raw_input('\nThe computer wins! Press ENTER to exit.')
					exit()
				else:
					computerMove = human.checkHit(computer.autoFire())
					if computerMove == False:
						pass
					else:
						humanBoard.placeMarker(human.checkHit(computer.autoFire()))
						self._clearScreen()
						humanBoard.display()
						print 'S = Ship; X = Hit; O = Miss'
						print '\nThe computer has attacked!\n'
						raw_input('Press ENTER to continue.')
						break

	def _validAttackCheck(self, attackInput):
		"""Determines attack input validity."""
		attackInput = list(attackInput) 
		inputLength = len(attackInput)
		if inputLength != 2 and inputLength != 3:
			return False
		letterList = []
		for i in xrange(10):
			letterList.append(uppercase[i])
		if attackInput[0].upper() not in letterList:
			return False
		try:
			if inputLength == 3:
				if int(str(attackInput[1]) + str(attackInput[2])) < 0 or int(str(attackInput[1]) + str(attackInput[2])) > 11:
					return False
			else:
				if int(attackInput[1]) < 0 or int(attackInput[1]) > 11:
					return False
		except ValueError:
			return False



