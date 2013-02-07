#!/usr/bin/python
from paymod import Rates, Account

rates = Rates()
acc = Account()

def mainMenu():
	print 'What would you like to do?'
	print '1). Enter price'
	print '2). Print table'
	print '3). Exit'
	while True:
		try:
			menuAns = input('--> ')
			if menuAns < 1 and menuAns > 3:
				print 'Invalid input.'
				tryAgain = raw_input('Press ENTER to continue.')
			else:
				return menuAns
		except (NameError, SyntaxError):
			print 'Invalid input.'
			tryAgain = raw_input('Press ENTER to continue.')

def main(menuAns):
	if menuAns == 1:
		while True:
			try:
				price = input('Enter a price: ')
				if price < 0:
					print 'Invalid input'
					tryAgain = raw_input('Press ENTER to continue.')
				else:
					acc.setPrice(price, rates.listRates())
					print 'Price is:', round(price, 2)
					moveAlong = raw_input('Press ENTER to continue.')
					break
			except (NameError, SyntaxError):
					print 'Invalid input.'
					tryAgain = raw_input('Press ENTER to continue.')

	elif menuAns == 2:
		i = 1
		print '%5s%15s%17s%11s%9s%19s' % \
			('Month', 'Current Total', 'Interest Amount',
			 'Principal', 'Payment', 'Balance Remaining')
		print '%5s%15s%17s%11s%9s%19s' % \
			('-' * 5, '-' * 13, '-' * 15, '-' * 9,
			'-' * 7, '-' * 17)

		while acc.currentBalance > 0.00:
			balanceRemaining = acc.currentBalance - acc.monthlyPayment
			if balanceRemaining < 0:
				balanceRemaining = 0
				acc.monthlyPayment = acc.currentBalance
			print '%5s%15.2f%17.2f%11.2f%9.2f%19.2f' % \
			(i, acc.currentBalance, acc.monthlyInterest, acc.monthlyPrincipal,
				acc.monthlyPayment, balanceRemaining)
			acc.currentBalance = acc.currentBalance - acc.monthlyPayment
			acc.monthlyInterest = balanceRemaining * rates.intRate
			acc.monthlyPayment = acc.monthlyPrincipal + acc.monthlyInterest
			i += 1
		moveAlong = raw_input('Press ENTER to continue.')

	elif menuAns == 3:
		exit()

while True:
	main(mainMenu())