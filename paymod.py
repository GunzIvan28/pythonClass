"""
Payment Info Class for the Tidbit Pay Program
"""
"""
 Month | Current Total | Interest Owed | Principal | Payment | Balance Remaining 

Balance Remaining = test
Testing again.
"""
class Item(object):
	"""Item information"""
	
	def __init__(self):
		self._basePrice = None
		self._downPayment = None
		self._interestRate = None

	def __str__(self):
		return 'The price is: ' + str(self._price)

	def setPrice(self, price, downPay, ):
		self._basePrice = price
		self._downPayment = price * .10

class Account(object):
	"""Account information"""

	def __init__(self):
		self._totalBalance = None

class Rates(object):
	"""Price rate information"""

	def __init__(self):
		self._downPay = .10
		self._monthlyIntRate = .01 # Annual rate per month
		self._