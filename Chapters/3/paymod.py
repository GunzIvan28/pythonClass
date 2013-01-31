class Rates(object):
	"""Rates information"""

	def __init__(self):
		self.downPay = .10
		self.interest = .01
		self.payment = .05

class Item(object):
	"""Item information"""
	
	def __init__(self, price, downRate, intRate, payRate):
		self.basePrice = price
		self.downPay = price * downRate
		self.interest = price * intRate
		self.startPrice = self.basePrice - self.downPay
		self.principal = price * payRate
		self.payment = self.principal + self.interest

	def __str__(self):
		return 'Base price: ' + str(self.basePrice) + \
		'\nDown Payment: ' + str(self.downPay) + \
		'\nStart Price: ' + str(self.startPrice) + \
		'\nInterest: ' + str(self.interest) + \
		'\nPrincipal: ' + str(self.principal) + \
		'\nPayment: ' + str(self.payment)

	def getPrice(self):
		return self.startPrice

class Account(object):
	"""Account information"""

	def __init__(self, price, payment):
		self.totalBalance = price - payment
		self.balRemaining = None

	def __str__(self):
		return 'Total Balance: ' + str(self.totalBalance)
