"""
Program: Battleship
Module: Players
Author: Bill Minear
"""
from random import randrange
from string import uppercase

class player(object):
	"""Player class and interactions."""

	def __init__(self, auto):
		"""auto == 0 means human, auto == 1 means computer."""
		self._ships = {'carrier':'5','battleship':'4','cruiser':'3','submarine':'3','destroyer':'2'}
		if auto == 0:
			"""Non-computer."""
			self._shipsAndCoords = {}
		elif auto == 1:
			self._shipsAndCoords = {'carrier':['B4','B5','B6','B7','B8'],
									'battleship':['A1','B1','C1','D1'],
									'cruiser':['J1','J2','J3'],
									'submarine':['E10','F10','G10'],
									'destroyer':['F5','F6']}
		self._attacks = []

	def storeShips(self, shipPlaceInfo):
		"""Store ship name and coordinates in dictionary for human player."""
		self._shipsAndCoords = shipPlaceInfo

	def checkHit(self, inputCoords):
		"""Checks if attack is a hit or miss and returns coords and marker."""
		for ship in self._shipsAndCoords:
			for coord in self._shipsAndCoords[ship]:
				if coord == inputCoords:
					self._shipsAndCoords[ship][self._shipsAndCoords[ship].index(coord)] = 'X'
					inputCoords = list(inputCoords)
					if len(inputCoords) == 3:
						hitOutcome = [inputCoords[0], inputCoords[1] + inputCoords[2], 'X']
						return hitOutcome
					else:
						hitOutcome = [inputCoords[0], inputCoords[1], 'X']
						return hitOutcome
		inputCoords = list(inputCoords)
		if len(inputCoords) == 3:
			hitOutcome = [inputCoords[0], inputCoords[1] + inputCoords[2], 'O']
			return hitOutcome
		else:
			hitOutcome = [inputCoords[0], inputCoords[1], 'O']
			return hitOutcome

	def checkWin(self):
		"""Checks all lists in self._shipsAndCoords for all X's indicating a win."""
		for ship in self._shipsAndCoords:
			for coord in self._shipsAndCoords[ship]:
				if coord != 'X':
					return False
		return True

	def autoFire(self):
		"""Random target selection for use by computer opponent."""
		while True:
			self._fireCoords = uppercase[randrange(1,10)] + str(randrange(1,10))
			if self._fireCoords in self._attacks:
				pass
			else:
				self.addToAttacks(self._fireCoords)
				return self._fireCoords

	def addToAttacks(self, coords):
		"""Used to generate a list of attacks so that they may not be repeated."""
		self._attacks.append(coords)

	def checkAttacks(self, coords):
		"""Used to check list of attacks so that an attack is not repeated."""
		if coords.upper() in self._attacks:
			return False


