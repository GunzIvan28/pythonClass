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

	def __init__(self,firstName='',lastName='',numberOfBooks=0):
		# Draw from fileInteraction. If no patron, return error.
		self._firstName = firstName 
		self._lastName = lastName 
		self._numberOfBooks = numberOfBooks

	def __str__(self):
		patronObject = [self._firstName,self._lastName,self._numberOfBooks]
		patronInfo = '|'.join(patronObject)
		return patronInfo

	def update(self, patronInfo):
		self._firstName = patronInfo[0]
		self._lastName = patronInfo[1]
		self._numberOfBooks = patronInfo[2]

	def addNumber(self):
		self._numberOfBooks = str(int(self._numberOfBooks) + 1)

	def subtractNumber(self):
		self._numberOfBooks = str(int(self._numberOfBooks) - 1)

	def listPatron(self):
		patronInfo = [self._firstName,self._lastName,self._numberOfBooks]
		return patronInfo

	def canCheckout(self):
		"""Returns True if patron can checkout based on number of
		already checked out books. False, otherwise."""
		if int(self._numberOfBooks) < 3:
			return True
		elif int(self._numberOfBooks) == 3:
			return False