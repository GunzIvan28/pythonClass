class player(object):

	def __init__(self):
		self._shipsAndCoords = {}

	def storeShips(self, shipPlaceInfo):
		self._shipsAndCoords = shipPlaceInfo

	def checkHit(self, inputCoords):
		for ship in self._shipsAndCoords:
			for coord in self._shipsAndCoords[ship]:
				if coord == inputCoords:
					self._shipsAndCoords[ship][self._shipsAndCoords[ship].index(coord)] = 'X'
					inputCoords = inputCoords.split('')
					hitOutcome = [inputCoords[0], inputCoords[1], 'X']
					return hitOutcome
				else:
					inputCoords = inputCoords.split('')
					hitOutcome = [inputCoords[0], inputCoords[1], 'O']
					return hitOutcome
