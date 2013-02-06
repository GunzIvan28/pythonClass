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
		print '2.) Print table'
		print '3.) Exit'
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
				if price < 0:
					print 'Price can not be less than zero.'
					tryAgain = raw_input('Press ENTER to try again.')
				else:
					acc.setPrice(price, rates.rateCalc(price))
					print 'Price set to $' + str(round(price, 2))
					moveOn = raw_input('Press ENTER to continue.')
					break
			except (NameError, SyntaxError):
				print 'Value not numeric. Press ENTER and try again.'

	elif menuAns == 2:
		if acc.accCheck() == 0:
			clrScr(osName)
			print '%5s%14s%16s%10s%8s%18s' % \
				('Month', 'Current Total', 'Interest Amount',
				 'Principal', 'Payment', 'Balance Remaining')
			print '%5s%14s%16s%10s%8s%18s' % \
				('-' * 5, '-' * 13, '-' * 15, '-' * 9,
				'-' * 7, '-' * 17)
			for i in xrange(acc.loanLength()):
				print acc.monthlyValues(i)
			carryOn = raw_input('Press ENTER to continue.')
		else:
			print 'Account does not exist.'
			carryOn = raw_input('Press ENTER to continue.')

	elif menuAns == 3:
		exit()

while True:
	"""Main loop"""
	main(mainMenu())

# current total = starting price - payment * i
# remaining balance = starting price - payment * (i + 1)
