class player(object):

	def __init__(self):
		self._shipsAndCoords = {}

	def storeShips(self, shipPlaceInfo):
		self._shipsAndCoords = shipPlaceInfo
		print self._shipsAndCoords

	def checkHit(self, coords):
		for ship in self._shipsAndCoords:
			print self._shipsAndCoords[ship]
