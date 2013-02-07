#!/usr/bin/python

"""
Program: Tid Bit Pay Plan Calculator 
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
	"""Utilization based on mainMenu() answer"""
	if menuAns == 1:
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

	elif menuAns == 2:
		clearScreen(osName)
		acc.printTable(rates.listRates())
		moveAlong = raw_input('Press ENTER to continue.')

	elif menuAns == 3:
		exit()

while True:
	main(mainMenu())