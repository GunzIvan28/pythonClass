from paymod import Rates, Account
import os

osName = os.name
rates = Rates()
acc = Account()

def clrScr(osName):
	"""Clears screen"""
	if osName == 'posix':
		os.system('clear')
	elif osName == 'dos' or osName == 'nt':
		os.system('cls')

def mainMenu():
	"""Action selection"""
	while True:
		clrScr(osName)
		print 'What would you like to do?'
		print '1.) Enter price'
		print '2.) Print Account Table'
		print '3.) Export to XML'
		print '4.) Exit'
		try:
			menuAns = input('--> ')
			if menuAns > 0 and menuAns <= 4:
				return menuAns
			else:
				tryAgain = raw_input('Invalid input. Press ENTER to try again.')
		except (NameError, SyntaxError):
			tryAgain = raw_input('Invalid input. Press ENTER to try again.')

def main(menuAns):
	"""Interactions based on mainMenu input"""
	if menuAns == 1:
		while True:
			try:
				price = input("Enter the item's value: ")
				acc.setPrice(price, rates.listRates())
				break
			except (NameError, SyntaxError):
				print 'Value not numeric. Press ENTER and try again.'

	elif menuAns == 2:
		accExist = acc.accCheck()
		if accExist == 0:
			clrScr(osName)
			print '%5s%14s%16s%10s%8s%18s' % \
				('Month', 'Current Total', 'Interest Amount',
				 'Principal', 'Payment', 'Balance Remaining')

			print '%5s%14s%16s%10s%8s%18s' % \
				('-' * 5, '-' * 13, '-' * 15, '-' * 9,
				'-' * 7, '-' * 17)

			for i in xrange(acc.loanLength()):
				print '%5d%14.2f%16.2f%10.2f%8.2f%18.2f' % \
					(i,
					acc.startPrice - acc.payment * i,
					acc.interest,
					acc.principal,
					acc.payment,
					acc.startPrice - acc.payment * (i + 1))
			carryOn = raw_input('Press ENTER to continue.')
		elif accExist == 1:
			print 'Account does not exist.'
			carryOn = raw_input('Press ENTER to continue.')

	elif menuAns == 4:
		exit()


while True:
	main(mainMenu())

# current total = starting price - payment * i
# remaining balance = starting price - payment * (i + 1)
