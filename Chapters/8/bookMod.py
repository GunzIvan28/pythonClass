"""
Program: Book Checkout Manager
Module: Book
Author: Bill Minear

Book:
	+) Title
		+) str(title)
	+) Author
		+) str(lastName, firstName)
	+) Current loanee
		+) str(lastName, firstName)
	+) Waiting list
		+) ['lastName, firstName']
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
		bookInfo = [self._title,self._author,self._loanee,self._waitList]
		return bookInfo

	def _prettifyName(self, name):
		self._nameSplit = name.split(',')
		self._nameSplit.reverse()
		self._prettyName = ' '.join(self._nameSplit)
		return self._prettyName.title()

	def _prettifyWaitList(self, waitList):
		self._waitListSplit = waitList.split(':')
		self._tempList = []
		for patron in self._waitListSplit:
			self._tempList.append(self._prettifyName(patron))
		self._prettyWaitList = ', '.join(self._tempList)
		return self._prettyWaitList

	def bookInfo(self):
		return 'Title: ' + self._title + '\n' + \
		'Author: ' + self._author + '\n' + \
		'Loanee: ' + self._prettifyName(self._loanee) + '\n' + \
		'Wait List: ' + self._prettifyWaitList(self._waitList)

	def available(self):
		if len(self._loanee) == 0:
			return True
		else:
			return False

	def nextInLine(self):
		"""lastname,firstname"""
		self._waitListSplit = self._waitList.split(':')
		print self._waitListSplit
		firstInLine = self._waitListSplit[0].split(' ')
		return firstInLine

	def waitListCheck(self, newLoanee, firstInLine):
		"""Combine with canCheckout patron method to determine result."""
		if newLoanee[0].lower() == firstInLine[0].lower() and newLoanee[1].lower() == firstInLine[1].lower():
			return True
		else:
			return False

	def appendWaitList(self, newLoanee):
		self._newLoanee = [newLoanee[1], newLoanee[0]]
		if len(self._waitList) == 0:
			self._waitList = ','.join(self._newLoanee)
		else:
			self._waitListSplit = self._waitList.split(':')
			self._waitListSplit.append(','.join(self._newLoanee))
			self._waitList = ':'.join(self._waitListSplit)

	def popList(self):
		self._waitListSplit = self._waitList.split(':')
		self._waitListSplit.pop(0)
		self._waitList = ':'.join(self._waitListSplit)

	def updateLoanee(self, loanee):
		self._newLoanee = [loanee[1],loanee[0]]
		self._loanee = ','.join(self._newLoanee)



# Need method to return next person in wait list.