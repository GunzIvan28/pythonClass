from random import randint
from string import uppercase

class player(object):

	def __init__(self, auto):
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

	def storeShips(self, shipPlaceInfo):
		self._shipsAndCoords = shipPlaceInfo

	def checkHit(self, inputCoords):
		"""Checks hit against player."""
		for ship in self._shipsAndCoords:
			for coord in self._shipsAndCoords[ship]:
				if coord == inputCoords:
					self._shipsAndCoords[ship][self._shipsAndCoords[ship].index(coord)] = 'X'
					inputCoords = list(inputCoords)
					hitOutcome = [inputCoords[0], inputCoords[1], 'X']
					return hitOutcome
				else:
					inputCoords = list(inputCoords)
					hitOutcome = [inputCoords[0], inputCoords[1], 'O']
					return hitOutcome

	# def checkHitComputer(self, inputCoords):
	# 	"""Checks hit against computer."""
	# 	for ship in self._autoShip:
	# 		for coord in self._autoShip[ship]:
	# 			if coord == inputCoords:
	# 				self._autoShip[ship][self._autoShip[ship].index(coord)] = 'X'
	# 				inputCoords = list(inputCoords)
	# 				hitOutcome = [inputCoords[0], inputCoords[1], 'X']
	# 				return hitOutcome
	# 	inputCoords = list(inputCoords)
	# 	hitOutcome = [inputCoords[0], inputCoords[1], 'O']
	# 	return hitOutcome

	def checkWin(self):
		for ship in self._shipsAndCoords:
			for coord in self._shipsAndCoords[ship]:
				print coord