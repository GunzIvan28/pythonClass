"""
Program: Book Checkout Manager
Module: Patron
Author: Bill Minear

Patron:
	+) Name
	+) Checked Out Books
		+) Can only have 3 at one time
"""

class patron(object):

	def __init__(self,patronInfo):
		# Draw from fileInteraction. If no patron, return error.
		self._firstName = patronInfo[0]
		self._lastName = patronInfo[1]
		self._numberOfBooks = patronInfo[2]

	def __str__(self):
		patronObject = [self._firstName,self._lastName,self._numberOfBooks]
		patronInfo = '|'.join(patronObject)
		return patronInfo
	
	def infoForFile(self):
		"""For passing to fileInteraction."""
		patronObject = [self._firstName,self._lastName,self._numberOfBooks]
		return patronObject
