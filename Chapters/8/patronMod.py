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

	def __init__(self):
		self._firstName = ''
		self._lastName = ''
		self._checkedOutBooks = []
		self._numberOfBooks = len(self._checkedOutBooks)

	def __str__(self):
		patronObject = [self._firstName,self._lastName]
		return patronObject

	