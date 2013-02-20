"""
Menus for the Payroll program.
"""

def mainMenu():
	while True:
		# clear()
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
		mainMenuAnswer = raw_input('--> ')
		try:
			if int(mainMenuAnswer) <  1 or int(mainMenuAnswer) > 5:
				raw_input('Invalid selection. Press ENTER to try again.')
			else:
				return mainMenuAnswer
		except ValueError:
				raw_input('Invalid input. Press ENTER to try again.')

def getEmployeeName():
	"""Takes first/last name as input and returns them in list format."""
	firstName = raw_input("Enter the employee's first name: ")
	lastName = raw_input("Enter the employee's last name: ")
	employeeName = [firstName, lastName]
	return employeeName

def newEmployee():
	"""Accepts first/last name, wage, and hours worked as input and returns them in list format."""
	employeeValues = getEmployeeName()
	hourlyWage = raw_input("Enter the employee's hourly wage: ")
	hoursWorked = raw_input("Enter the number of hours worked: ")
	employeeValues.extend([hourlyWage, hoursWorked])
	return employeeValues

