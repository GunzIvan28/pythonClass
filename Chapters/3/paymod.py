class Rates(object):
	"""Rates information"""

	def __init__(self):
		self.downPay = .10
		self.interest = .01
		self.payment = .05

	def itemCalcs(self, price):
		"""Calculates rates for an item"""
		self.calcs = [
		price,
		price * self.downPay,
		price * self.interest,
		price * self.payment
		]
		return self.calcs

class Account(object):
	"""Account information"""

	def __init__(self, rateList):
		self.basePrice = rateList[0] 
		self.downPay = rateList[1]
		self.interest = rateList[2]
		self.startPrice = self.basePrice - self.downPay
		self.principal = rateList[3]
		self.payment = self.principal + self.interest
		self.totalBalance = None
		self.balRemaining = None

	def __str__(self):
		return 'Base price: ' + str(self.basePrice) + \
		'\nDown Payment: ' + str(self.downPay) + \
		'\nStart Price: ' + str(self.startPrice) + \
		'\nInterest: ' + str(self.interest) + \
		'\nPrincipal: ' + str(self.principal) + \
		'\nPayment: ' + str(self.payment) + \
		'\nTotal Balance: ' + str(self.totalBalance)

	def getPrice(self):
		return self.startPrice

	def setBalance(self, price, payment):
		self.totalBalance = price - payment
		self.balRemaining = None

