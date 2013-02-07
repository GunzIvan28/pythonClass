#!/usr/bin/python

"""
Program: TidBit Pay Plan Calculator 
		-or- 'How I learned to hate accounting.'
Author: Bill Minear

Purpose:
	Accepts an inventory item price as input and 
	calculates loan amounts

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
	clearScreen(osName)	
	print 'What would you like to do?'
	print '1). Enter price'
	print '2). Print table'
	print '3). Exit'
	while True:
		try:
			menuAnswer = input('--> ')
			if menuAnswer < 1 and menuAnswer > 3:
				print 'Invalid input.'
				tryAgain = raw_input('Press ENTER to continue.')
			else:
				return menuAnswer
		except (NameError, SyntaxError):
			print 'Invalid input.'
			tryAgain = raw_input('Press ENTER to continue.')

def main(menuAnswer):
	"""Utilization based on mainMenu return"""
	if menuAnswer == 1:
		try:
			price = input('Enter a price: ')
			if price < 0:
				print '\nInvalid input.\n'
				tryAgain = raw_input('Press ENTER to continue.')
			else:
				acc.setPrice(price, rates.listRates())
				print '\nPrice is: $%.2f' % price
				moveAlong = raw_input('\nPress ENTER to continue.')
		except (NameError, SyntaxError):
				print '\nInvalid input.\n'
				tryAgain = raw_input('Press ENTER to continue.')

	elif menuAnswer == 2:
		if acc.doesAccountExist() == 0:
			print '\nNo price has been set.'
			tryAgain = raw_input('\nPress ENTER to continue.')
		else:
			clearScreen(osName)
			acc.setPrice(acc.price, rates.listRates())	# <- This is here because of my
			print acc.currentBalance					# poorly designed data manipulation.
			moveAlong = raw_input('Press ENTER to continue.')

	elif menuAnswer == 3:
		exit()

while True:
	main(mainMenu())