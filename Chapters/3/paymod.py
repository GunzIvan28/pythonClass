class Rates(object):
	"""Rates information"""

	def __init__(self):
		self.downPay = .10
		self.interest = .01
		self.payment = .05

	def listRates(self):
		rates = [self.downPay, self.interest, self.payment]
		return rates

class Account(object):
	"""Account information"""

	def __init__(self, price, rates):
		self.basePrice = price
		self.downPay = price * rates[0] 
		self.interest = price * rates[1]
		self.startPrice = self.basePrice - self.downPay
		self.principal = self.startPrice * rates[2]
		self.payment = self.principal + self.interest

	def __str__(self):
		"""For debugging"""
		return 'Base price: ' + str(self.basePrice) + \
		'\nDown Payment: ' + str(self.downPay) + \
		'\nStart Price: ' + str(self.startPrice) + \
		'\nInterest: ' + str(self.interest) + \
		'\nPrincipal: ' + str(self.principal) + \
		'\nPayment: ' + str(self.payment) + \
		'\nTotal Balance: ' + str(self.totalBalance)

 	def loanLength(self):
		payTotal = [self.payment]
		while payTotal[-1] < self.startPrice:
			payTotal.append(payTotal[-1] + self.payment)
		return len(payTotal)
