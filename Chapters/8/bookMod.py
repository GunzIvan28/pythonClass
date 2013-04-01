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

	def __init__(self):
		self._title = ''
		self._author = ''
		self._loanee = ''
		self._waitList = []

	def __str__(self):
		bookObject = [self._title, self._author,
						self._loanee, self._waitList]
		return bookObject