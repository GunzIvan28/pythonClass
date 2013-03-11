"""
Employee Class for Payroll program.
"""

class employee(object):
	"""Class for storing employee values temporarily"""

	def __init__(self, employeeInfo):
		self.firstName		= employeeInfo[0]
		self.lastName		= employeeInfo[1]
		self.hourlyWage		= employeeInfo[2]
		self.hoursWorked	= employeeInfo[3]

	def __str__(self):
		return str(self.firstName) + '\n' + \
		str(self.lastName) + '\n' + \
		str(self.hourlyWage) + '\n' + \
		str(self.hoursWorked)

	# def setAttributes(employeeValues):
	# 	self.firstName = employeeValues[0]
	# 	self.lastName = employeeValues[1]
	# 	self.hourlyWage = employeeValues[2]
	# 	self.hoursWorked = employeeValues[3]

	def getPay(self):
		pay = float(self.hourlyWage) * float(self.hoursWorked)
		return float(pay)

	def returnAttributes():
		employeeInfo = [self.firstName,
						self.lastName,
						self.hourlyWage,
						self.hoursWorked]
		return employeeInfo