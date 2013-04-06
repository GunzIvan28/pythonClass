"""
Program: Book Checkout Manager
Module: Patron
Author: Bill Minear
"""

class patron(object):

	def __init__(self,firstName='',lastName='',numberOfBooks=0):
		self._firstName = firstName 
		self._lastName = lastName 
		self._numberOfBooks = numberOfBooks

	def __str__(self):
		patronObject = [self._firstName,self._lastName,self._numberOfBooks]
		patronInfo = '|'.join(patronObject)
		return patronInfo

	def update(self, patronInfo):
		"""Update patron info by passing in a list."""
		self._firstName = patronInfo[0]
		self._lastName = patronInfo[1]
		self._numberOfBooks = patronInfo[2]

	def addNumber(self):
		"""Add one to checked out book count when patron checks out a book."""
		self._numberOfBooks = str(int(self._numberOfBooks) + 1)

	def subtractNumber(self):
		"""Remove one from checked out book count when patron checks out a book."""
		self._numberOfBooks = str(int(self._numberOfBooks) - 1)

	def listPatron(self):
		"""Return patron info in list format."""
		patronInfo = [self._firstName,self._lastName,self._numberOfBooks]
		return patronInfo

	def canCheckout(self):
		"""Returns True if patron can checkout based on number of
		already checked out books. False, otherwise."""
		if int(self._numberOfBooks) < 3:
			return True
		elif int(self._numberOfBooks) == 3:
			return False