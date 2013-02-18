"""
Employee Module
"""
from os.path import exists
from xml.dom import minidom

def employeeCheck(firstName, lastName):
	"""Looks for an employee in employeeData.xml"""
	employeeDataXml = minidom.parse('employeeData.xml')
	root = employeeDataXml.documentElement
	employees = employeeDataXml.getElementsByTagName('Employee')
	for employee in employees:
		firstNameNodes = employee.getElementsByTagName('Firstname')[0].childNodes
		for firstNameNode in firstNameNodes:
			if firstNameNode.data == firstName.lower():
				lastNameNodes = employee.getElementsByTagName('Lastname')[0].childNodes
				for lastNameNode in lastNameNodes:
					if lastNameNode.data == lastName.lower():
						root.unlink()
						return True
					else:
						root.unlink()
						return False
			else:
				root.unlink()
				return False



def fileCheck():
	"""Creates file and/or verifies file mutability."""
	if exists('employeeData.xml'):
		try:
			xml = open('employeeData.xml', 'r')
			xml.close()
			return 0 
		except IOError:
			return 1 
	else:
		try:
			newXml = minidom.Document()
			rootElement = newXml.createElement('Employees')
			newXml.appendChild(rootElement)
			newFile = open('employeeData.xml', 'w')
			newXml.writexml(newFile)
			newFile.close()
			return 0
		except IOError:
			return 2


class employee(object):
	"""Class for manipulating employee payroll information."""

	def __init__(self):
		self.firstName = None
		self.lastName = None
		self.hourlyWage = None
		self.hoursWorked = None
		# self.pathToEmployeeData = 'employeeData.xml'

	def __str__(self):
		return str(self.firstName) + '\n' + \
		str(self.lastName) + '\n' + \
		str(self.hourlyWage) + '\n' + \
		str(self.hoursWorked)

	def setEmployee(self, firstName, lastName, hourlyWage, hoursWorked):
		"""Assign values to employee attributes."""
		self.firstName = firstName.lower()
		self.lastName = lastName.lower()
		self.hourlyWage = str(float(hourlyWage))
		self.hoursWorked = str(float(hoursWorked))

	def employeeToXML(self):
		"""For testing"""
		doc = minidom.Document()
		root = doc.createElement('Employees')
		doc.appendChild(root)
		""" Need 'Employee' child """
		list = ['firstName', 'lastName', 'hourlyWage', 'hoursWorked']
		for each in list:
			child = doc.createElement(each.title())
			root.appendChild(child)
			childValue = doc.createTextNode(getattr(self,each))
			child.appendChild(childValue)
		f = open('employeeData.xml', 'w')
		root.writexml(f)
		f.close()

	def addEmployee(self):
		"""Append employee to employeeData.xml"""
		employeeDataXml = minidom.parse('employeeData.xml')
		root = employeeDataXml.documentElement
		employee = employeeDataXml.createElement('Employee')
		root.appendChild(employee)
		list = ['firstName', 'lastName', 'hourlyWage', 'hoursWorked']
		for element in list:
			child = employeeDataXml.createElement(element.title())
			employee.appendChild(child)
			childValue = employeeDataXml.createTextNode(str(getattr(self,element)))
			child.appendChild(childValue)
		employeeDataFile = open('employeeData.xml', 'w')
		root.writexml(employeeDataFile)
		employeeDataFile.close()
		root.unlink()





"""
Needed XML abilities:
	+) Does file exist?
		+) If no: 
			+) Create file, add header and employee root.
		+) If yes: 
			+) Read in, set employee as root, and append
				new employees, read employee info for output,
				etc.
"""
