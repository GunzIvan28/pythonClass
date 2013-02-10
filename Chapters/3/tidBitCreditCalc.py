#!/usr/bin/python

"""
Program: TidBit Pay Plan Calculator 
		-or- 'How I learned to hate accounting.'
Author: Bill Minear

Purpose:
	Accepts a dollar value as input and 
	calculates loan amounts.

"""
import os
from paymod import Rates, Account

osName = os.name
rates = Rates()
acc = Account()

def clearScreen(osName):
	"""Clears screen"""
	if osName == 'posix':
		os.system('clear')
	elif osName == 'dos' or osName == 'nt':
		os.system('cls')

def mainMenu():
	"""Action selection"""
	while True:
		try:
			clearScreen(osName)	
			print 'What would you like to do?'
			print '1). Enter price'
			print '2). Print table'
			print '3). Exit'
			menuAnswer = input('--> ')
			if menuAnswer < 1 or menuAnswer > 3:
				print '\nInvalid input.'
				tryAgain = raw_input('\nPress ENTER to continue.')
			else:
				return menuAnswer
		except (NameError, SyntaxError):
			print '\nInvalid input.'
			tryAgain = raw_input('\nPress ENTER to continue.')

def main(menuAnswer):
	"""Utilization based on mainMenu return."""
	if menuAnswer == 1:
		try:
			price = input('\nEnter a price: ')
			if price < 0:
				print '\nInvalid input.\n'
				tryAgain = raw_input('Press ENTER to continue.')
			else:
				acc.setPrice(price, rates.listRates())
				print '\nPrice set to: $%.2f' % price
				moveAlong = raw_input('\nPress ENTER to continue.')
		except (NameError, SyntaxError):
				print '\nInvalid input.\n'
				tryAgain = raw_input('Press ENTER to continue.')

	elif menuAnswer == 2:
		if acc.doesAccountExist() == 0:
			print '\nNo price has been set.\n'
			tryAgain = raw_input('Press ENTER to continue.')
		else:
			clearScreen(osName)
			acc.setPrice(acc.price, rates.listRates())	# <- This is here because of my  
			acc.printTable(rates.listRates())			# poorly designed data manipulation.
			moveAlong = raw_input('Press ENTER to continue.')

	elif menuAnswer == 3:
		exit()

# Main loop.
while True:
	main(mainMenu())