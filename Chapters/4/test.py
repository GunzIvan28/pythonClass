#!/usr/bin/python

from time import sleep
from menu import clear		# Mine
from payroll import *		# Mine

fileCheckValue = None
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

	if mainMenuAnswer == 2:
		firstName = raw_input('Employee first name: ')
		lastName = raw_input('Employee last name: ')
		doesEmployeeExist = employeeCheck(firstName, lastName)
		if doesEmployeeExist == True:
			print '\nEmployee already exists.\n'
			print 'Select Update Employee or Add/Remove Employee'
			print 'at the main menu to modify an existing record.\n'
			raw_input('Press ENTER to return to the main menu.')
		elif doesEmployeeExist == False:
			while True:
				try:
					hourlyWage = input('Hourly wage: ')
					if hourlyWage < 0:
						print 'Hourly wage must be higher than zero.'
						raw_input('Press ENTER to input a new wage.')
					else:
						break
				except (NameError, SyntaxError):
					raw_input('Invalid input. Press ENTER to try again.')
			while True:
				try:
					hoursWorked = input('Hours worked: ')
					if hoursWorked < 0:
						print 'Hours worked cannot be less than zero.'
						raw_input('Press ENTER to input a new wage.')
					else:
						break
				except (NameError, SyntaxError):
					raw_input('Invalid input. Press ENTER to try again.')
			while True:
				clear()
				print 'Before the new user is added, please verify the following:'
				print 'First Name:', firstName
				print 'Last Name:', lastName
				print 'Hourly Wage: $%.2f/hr' % hourlyWage
				print 'Hours Worked: %.2f' % hoursWorked
				print 'Is this information correct?'
				isInputCorrect = raw_input('(y/n) --> ')
				if isInputCorrect == 'y':
					employee.setEmployee(firstName, lastName, hourlyWage, hoursWorked)
					employee.addEmployee()
					print 'Employee successfully added.'
					raw_input('Press ENTER to continue.')
					break
				elif isInputCorrect == 'n':
					print 'No employee information has been saved.'
					raw_input('Press ENTER to return to the main menu.')
					break
				else:
					raw_input('Please answer y or n. Press ENTER to continue.')

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
			print "or check the program's directory permissions.\n"
			raw_input('Press ENTER to exit the program.')
			exit()
	main(mainMenu())