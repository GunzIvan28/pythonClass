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

	def __init__(self, bookInfo = []):
		if len(bookInfo) > 0:
			self._title = bookInfo[0] 
			self._author = bookInfo[1]
			self._loanee = bookInfo[2]
			self._waitList = bookInfo[3]
		else:
			self._title = ''
			self._author = ''
			self._loanee = ''
			self._waitList = []

	def __str__(self):
		return 'Title: ' + self._title + '\n' + \
		'Author: ' + self._author + '\n' + \
		'Loanee: ' + self._loanee + '\n' + \
		'Wait List: ' + self._waitList
		# bookObject = [self._title, self._author,
		# 				self._loanee, self._waitList]
		# bookInfo = '|'.join(bookObject)
		# return bookInfo

	# def displayBookInfo(self):

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
