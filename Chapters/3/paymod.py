class Rates(object):
	"""Rate information"""

	def __init__(self):
		self.downPay = .10
		self.interest = .01
		self.payment = .05

	def rateCalc(self, price):
		"""[0]Down Payment [1]Interest [2]Monthly Payment"""
		rates = [
			self.downPay * price,
			self.interest * price,
			self.payment * (price - (price * self.downPay))
			]
		return rates

class Account(object):
	"""Account information"""

	def __init__(self):
		self.basePrice = None
		self.downPay = None
		self.interest = None
		self.startPrice = None
		self.principal = None
		self.payment = None

	def __str__(self):
		"""For debugging"""
		return 'Base price: ' + str(self.basePrice) + \
		'\nDown Payment: ' + str(self.downPay) + \
		'\nStart Price: ' + str(self.startPrice) + \
		'\nInterest: ' + str(self.interest) + \
		'\nPrincipal: ' + str(self.principal) + \
		'\nPayment: ' + str(self.payment) + \
		'\nTotal Balance: ' + str(self.totalBalance)

	def accCheck(self):
		if self.basePrice != None:
			return 0

	def setPrice(self, price, rates):
		"""Sets price and related payments"""
		self.basePrice = price
		self.downPay = rates[0] 
		self.interest = rates[1]
		self.startPrice = self.basePrice - self.downPay
		self.principal = rates[2]
		self.payment = self.principal + self.interest

 	def loanLength(self):
		payTotal = [self.payment]
		while payTotal[-1] < self.startPrice:
			payTotal.append(payTotal[-1] + self.payment)
		return len(payTotal)

	def monthlyValues(self, month):
		balRemain = self.startPrice - self.payment * (month + 1)
		if balRemain == 0 or balRemain < 0:
			return '%5d%14.2f%16.2f%10.2f%8.2f%18.2f' % \
			(month + 1,
			self.startPrice - self.payment * month,
			self.interest,
			self.principal,
			self.startPrice - self.payment * month,
			0)
		else:
			return '%5d%14.2f%16.2f%10.2f%8.2f%18.2f' % \
			(month + 1,
			self.startPrice - self.payment * month,
			self.interest,
			self.principal,
			self.payment,
			balRemain)
