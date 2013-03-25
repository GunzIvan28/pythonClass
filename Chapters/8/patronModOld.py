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
		patronFile.write((','.join([str(self._patronID),self._firstName,self._lastName]) + '\n'))
		patronFile.close()

	def check(self, patronID=0, firstName='', lastName=''):
		"""Checks file for existing patron."""
		if patronID != 0:
			patronFile = open('patronFile.txt', 'r')
			for line in patronFile:
				line = line.split(',')
				if line[0] == str(patronID):
					patronFile.close()
					return True
			return False
		if lastName != '':
			patronFile = open('patronFile.txt', 'r')
			for line in patronFile:
				line = line.rstrip('\n').split(',')
				if line[2] == lastName and line[1] == firstName:
					patronFile.close()
					return True
			return False

	def newID(self):
		"""Checks last line of file for ID and returns ID + 1.
		Used for creating new patrons."""
		patronFile = open('patronFile.txt', 'r')
		for line in patronFile:
			if line == '':
				return 1
			else:
				pass
		lastLine = line
		patronFile.close()
		print lastLine
		# return int(lastLine[0]) + 1





