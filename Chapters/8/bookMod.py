"""
Program: Book Checkout Manager
Module: Book
Author: Bill Minear
"""
class book(object):

	def __init__(self, bookInfo):
		if len(bookInfo) == 2:
			self._title = bookInfo[0] 
			self._author = bookInfo[1]
			self._loanee = ''
			self._waitList = ''
		else:
			self._title = bookInfo[0] 
			self._author = bookInfo[1]
			self._loanee = bookInfo[2]
			self._waitList = bookInfo[3]

	def __str__(self):
		return 'Title: ' + self._title + '\n' + \
		'Author: ' + self._author + '\n' + \
		'Loanee: ' + self._loanee + '\n' + \
		'Wait List: ' + self._waitList

	def listBookInfo(self):
		"""Returns book info in list format."""
		bookInfo = [self._title,self._author,self._loanee,self._waitList]
		return bookInfo

	def _prettifyName(self, name):
		"""Turns lastname,firstname into Firstname Lastname."""
		self._nameSplit = name.split(',')
		self._nameSplit.reverse()
		self._prettyName = ' '.join(self._nameSplit)
		return self._prettyName.title()

	def _prettifyWaitList(self, waitList):
		"""Turns lastname,firstname:lastname,firstname into Firstname Lastname, Firstname Lastname."""
		self._waitListSplit = waitList.split(':')
		self._tempList = []
		for patron in self._waitListSplit:
			self._tempList.append(self._prettifyName(patron))
		self._prettyWaitList = ', '.join(self._tempList)
		return self._prettyWaitList

	def outputBookInfo(self):
		"""Returns book info in pretty format."""
		return 'Title: ' + self._title + '\n' + \
		'Author: ' + self._author + '\n' + \
		'Loanee: ' + self._prettifyName(self._loanee) + '\n' + \
		'Wait List: ' + self._prettifyWaitList(self._waitList)

	def available(self):
		"""Returns True if book is not already checked out, returns False otherwise."""
		if len(self._loanee) == 0:
			return True
		else:
			return False

	def appendWaitList(self, newLoanee):
		"""Adds patron name to end of wait list if book is checked out."""
		self._newLoanee = [newLoanee[1], newLoanee[0]]
		if len(self._waitList) == 0:
			self._waitList = ','.join(self._newLoanee)
		else:
			self._waitListSplit = self._waitList.split(':')
			self._waitListSplit.append(','.join(self._newLoanee))
			self._waitList = ':'.join(self._waitListSplit)

	def popList(self):
		"""Removes first person on wait list and places them into loanee."""
		self._waitListSplit = self._waitList.split(':')
		if len(self._waitListSplit) == 0:
			self._loanee = ''
		else:
			self._loanee = self._waitListSplit.pop(0)
		self._waitList = ':'.join(self._waitListSplit)

	def getLoanee(self):
		"""Returns current loanee name."""
		if self._loanee == '':
			return self._loanee
		else:
			self._loaneeName = self._loanee.split(',')
			self._loaneeName.reverse()
			return self._loaneeName

	def updateLoanee(self, loanee):
		"""Adds loanee name to self._loanee if book is not checked out."""
		"""If book is checked out and returned, loanee is updated automatically via wait list."""
		self._newLoanee = [loanee[1],loanee[0]]
		self._loanee = ','.join(self._newLoanee)
