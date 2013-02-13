#!/usr/bin/python

from time import sleep
from menu import clear			# Mine
from payroll import employee	# Mine
employee = employee()

def mainMenu():
	while True:
		try:
			clear()
			print '-' * 14 
			print 'Payroll System'
			print '-' * 14 
			print '\nWhat would you like to do?'
			print '-' * 26
			print '1.) View employee report'
			print '2.) Add new employee'
			print '3.) Update employee'
			print '4.) Remove employee'
			print '5.) Exit'
			mainMenuAnswer = input('--> ')
			if mainMenuAnswer <  1 or mainMenuAnswer > 5:
				tryAgain = raw_input('Invalid selection. Press ENTER to try again.')
			else:
				return mainMenuAnswer
		except (NameError, SyntaxError):
			tryAgain = raw_input('Invalid selection. Press ENTER to try again.')

def main(mainMenuAnswer):
	# if mainMenuAnswer == 1:

	# if mainMenuAnswer == 2:

	# if mainMenuAnswer == 3:

	# if mainMenuAnswer == 4:

	if mainMenuAnswer == 5:
		clear()
		exit()


while True:
	main(mainMenu())