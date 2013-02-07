class Rates(object):
	"""Rate information"""

	def __init__(self):
		self.downRate = .10
		self.intRate = .01
		self.payRate = .05

	def listRates(self):
		"""[0]Down Payment [1]Interest [2]Monthly Payment"""
		rates = [self.downRate, self.intRate, self.payRate]
		return rates

class Account(object):
	"""Account information"""

	def __init__(self):
		self.downPayment = None
		self.base = None
		self.currentBalance = None
		self.monthlyPrincipal = None
		self.monthlyInterest = None
		self.monthlyPayment = None

	# def __str__(self):
	# 	"""For debugging"""
	# 	return 'Base price: ' + str(self.basePrice) + \
	# 	'\nDown Payment: ' + str(self.downPay) + \
	# 	'\nStart Price: ' + str(self.startPrice) + \
	# 	'\nInterest: ' + str(self.interest) + \
	# 	'\nPrincipal: ' + str(self.principal) + \
	# 	'\nPayment: ' + str(self.payment) + \
	# 	'\nTotal Balance: ' + str(self.totalBalance)

	# def accCheck(self):
	# 	if self.basePrice != None:
	# 		return 0

	def setPrice(self, price, rates):
		"""Sets price and related payments"""
		self.downPayment = price * rates[0]
		self.base = price - self.downPayment
		self.currentBalance = self.base
		self.monthlyPrincipal = self.base * rates[2]
		self.monthlyInterest = self.currentBalance * rates[1]
		self.monthlyPayment = self.monthlyPrincipal + self.monthlyInterest

#  	def loanLength(self):
# 		payTotal = [self.payment]
# 		while payTotal[-1] < self.curPrice:
# 			payTotal.append(payTotal[-1] + self.payment)
# 		return len(payTotal)

# 	def monthlyValues(self, month):
# 		self.payment = 
# 		balRemain = self.startPrice - self.payment * (month + 1)
# 		self.curPrice = self.startPrice - self.payment * month
# 		if balRemain == 0 or balRemain < 0:
# 			return '%5d%14.2f%16.2f%10.2f%8.2f%18.2f' % \
# 			(month + 1,
# 			curPrice,
# 			self.interest * curPrice,
# 			self.principal,
# 			curPrice,
# 			0)
# 		else:
# 			return '%5d%14.2f%16.2f%10.2f%8.2f%18.2f' % \
# 			(month + 1,
# 			curPrice,
# 			self.interest * curPrice,
# 			self.principal,
# 			self.principal + (self.interest * curPrice),
# 			balRemain)

# # Calculate interest based on current balance.