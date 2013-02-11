"""
Employee Module
"""

class employee(object):

	def __init__(self):
		self.firstName = None
		self.lastName = None
		self.hourlyWage = None
		self.hoursWorked = None

	def __str__(self):
		return str(self.firstName) + '\n' + \
		str(self.lastName) + '\n' + \
		str(self.hourlyWage) + '\n' + \
		str(self.hoursWorked)

	def setEmployee(self, firstName, lastName, hourlyWage, hoursWorked):
		self.firstName = firstName
		self.lastName = lastName
		self.hourlyWage = hourlyWage
		self.hoursWorked = hoursWorked
