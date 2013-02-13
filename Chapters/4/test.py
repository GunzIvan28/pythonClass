#!/usr/bin/python

from time import sleep
from menu import clear		# Mine
from payroll import *		# Mine

employee = employee()
fileCheckValue = None

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

# Check on program start.
#	If exists, fileCheckValue = 0 
#	If not and created, fileCheckValue = 0
#	If failed for:
#		Unable to open existing
#			fileCheckValue = 1
#		Unable to create
#			fileCheckValue = 2

while True:
	while fileCheckValue == None:
		fileCheckValue = fileCheck()
		if fileCheckValue == 0:
			pass
		elif fileCheckValue == 1:
			print 'Unable to read employeeReport.xml. Check file permissions.'
			raw_input('Press ENTER to exit the program.')
			exit()
		elif fileCheckValue == 2:
			print 'employeeReport.xml could not be created.\n'
			print 'Manually create the file in the program directory '
			print "or check the program's directory permissions."
			raw_input('Press ENTER to exit the program.')
			exit()
	main(mainMenu())