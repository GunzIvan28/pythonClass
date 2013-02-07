"""
paymod.py
Author: Bill Minear

Purpose: 
	Contains classes available for use 
	in the TidBit Pay Plan Calculator.

Classes:
	Rates:
		Exists in case the ability to modify rates was
		desired in the future and for data separation and
		modularity.

		Methods:
			listRates:
				Returns rates in list format.

	Account:
		Stores information frequently utilized in main.py.

		Methods:
			setPrice:
				Accepts a price and rates as input. Calculates
				information needed for displaying output related
				to the loan.

			doesAccountExist:
				Ensures account information is populated.

			printTable:
				Prints the account information in a fancy table.
"""

class Rates(object):
	"""Rate information"""

	def __init__(self):
		self.downRate = .10
		self.payRate = .05
		self.intRate = .01

	def listRates(self):
		"""[0]Down Payment [1]Monthly Payment [2]Interest"""
		rates = [self.downRate, self.payRate, self.intRate]
		return rates

class Account(object):
	"""Account information"""

	def __init__(self):
		self.price = None
		self.downPayment = None
		self.base = None
		self.currentBalance = None
		self.monthlyPrincipal = None
		self.monthlyInterest = None
		self.monthlyPayment = None

	def setPrice(self, price, rates):
		"""Sets price and related payments"""
		self.price = price
		self.downPayment = self.price * rates[0]
		self.base = self.price - self.downPayment
		self.currentBalance = self.base
		self.monthlyPrincipal = self.base * rates[1]
		self.monthlyInterest = self.currentBalance * rates[2]
		self.monthlyPayment = self.monthlyPrincipal + self.monthlyInterest

	def doesAccountExist(self):
		"""To ensure that the account attributes have been populated."""
		if self.price == None:
			return 0
		else:
			return 1

	def printTable(self, rates):
		"""Cluster f*** central"""
		i = 1
		print '\nItem Price: $%.2f | Down Payment: $%.2f' % (self.price, self.downPayment)
		print '%5s%15s%17s%11s%9s%19s' % \
			('-' * 5, '-' * 13, '-' * 15, '-' * 9, '-' * 7, '-' * 17)
		print '%5s%15s%17s%11s%9s%19s' % \
			('Month', 'Current Total', 'Interest Amount',
			 'Principal', 'Payment', 'Balance Remaining')
		print '%5s%15s%17s%11s%9s%19s' % \
			('-' * 5, '-' * 13, '-' * 15, '-' * 9, '-' * 7, '-' * 17)
		while self.currentBalance > 0.00:
			balanceRemaining = self.currentBalance - self.monthlyPayment
			if balanceRemaining < 0:
				balanceRemaining = 0
				self.monthlyPayment = self.currentBalance
			print '%5s%15.2f%17.2f%11.2f%9.2f%19.2f' % \
			(i, self.currentBalance, self.monthlyInterest, self.monthlyPrincipal,
				self.monthlyPayment, balanceRemaining)
			self.currentBalance = self.currentBalance - self.monthlyPayment
			self.monthlyInterest = balanceRemaining * rates[2]
			self.monthlyPayment = self.monthlyPrincipal + self.monthlyInterest
			i += 1
