"""
Program: Library Checkout Manager
Module: Patron
Author: Bill Minear

Patron:
	+) Name
	+) Checked Out Books
		+) Can only have 3 at one time
	+) PatronID*
		+) Requires knowledge of stored data.
		+) By parsing stored data:
			+) Recurring patrons can be instantiated
			+) New patrons can be assigned next-in-line patronIDs.

"""

class patron(object):

	def __init__(self):
		self._patronID = 0 
		self._firstName = ''
		self._lastName = '' 
		self._checkedOutBooks = []
		self._numberOfBooks = len(self._checkedOutBooks)

	def __str__(self):
		patronObject = [str(self._patronID),self._firstName,self._lastName]
		return patronObject

	def new(self, patronID, firstName, lastName):
		"""Arguments are firstName, lastName, and patronID."""  
		self._patronID = patronID
		self._firstName = firstName
		self._lastName = lastName
		patronFile = open('patronFile.txt', 'a')
		patronFile.write('\n' + ','.join([str(self._patronID),self._firstName,self._lastName]))
		patronFile.close()


