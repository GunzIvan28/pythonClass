"""
Employee Module
"""

class employee(object):

	def __init__(self):
		self.firstName = None
		self.lastName = None
		self.hourlyWage = None
		self.hoursWorked = None

	def setEmployee(self, firstName, lastName, hourlyWage, hoursWorked):
		self.firstName = firstName
		self.lastName = lastName
		self.hourlyWage = hourlyWage
		self.hoursWorked = hoursWorked
