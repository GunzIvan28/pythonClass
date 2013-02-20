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
				# Return value maybe needs to be an integer?
				return mainMenuAnswer
		except ValueError:
				raw_input('Invalid input. Press ENTER to try again.')

def getEmployeeName():
	"""Takes first/last name as input and returns them in list format."""
	firstName = raw_input("Enter the employee's first name: ")
	lastName = raw_input("Enter the employee's last name: ")
	employeeName = [firstName.lower(), lastName.lower()]
	return employeeName

def newEmployee():
	"""Takes first/last name, wage, and hours worked as input and returns them in list format."""
	newEmployeeValues = getEmployeeName()
	while True:
		hourlyWage = raw_input("Enter the employee's hourly wage: ")
		try:
			if float(hourlyWage) <= 0:
				raw_input('Wage can not be less than zero. Press ENTER to try again.')
			else:
				hourlyWage = float(hourlyWage)
				break
		except ValueError:
			raw_input('Invalid input. Press ENTER to try again.')
	while True:
		hoursWorked = raw_input("Enter the number of hours worked: ")
		try:
			if float(hoursWorked) < 0:
				raw_input('Hours worked can not be less than zero. Press ENTER to try again.')
			else:
				hoursWorked = float(hoursWorked)
				break
		except ValueError:
			raw_input('Invalid input. Press ENTER to try again.')
	newEmployeeValues.extend([hourlyWage, hoursWorked])
	return newEmployeeValues

