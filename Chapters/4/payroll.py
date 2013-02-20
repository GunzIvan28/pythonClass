"""
Employee Module
"""
from os.path import exists
from xml.dom import minidom

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

def employeeCheck(firstName, lastName):
	"""Looks for an employee in employeeData.xml"""
	employeeDataXml = minidom.parse('employeeData.xml')
	employees = employeeDataXml.getElementsByTagName('Employee')
	if len(employees) == 0:
		employeeDataXml.unlink()
		return False
	else:
		for employee in employees:
			firstNameNode = employee.getElementsByTagName('Firstname')[0].childNodes[0].data
			lastNameNode = employee.getElementsByTagName('Lastname')[0].childNodes[0].data
			if firstNameNode == firstName.lower() and lastNameNode == lastName.lower():
				employeeDataXml.unlink()
				return True
		employeeDataXml.unlink()
		return False

def addEmployee(firstName, lastName, hourlyWage, hoursWorked):
	"""Append employee to employeeData.xml"""
	employeeDataXml = minidom.parse('employeeData.xml')
	root = employeeDataXml.documentElement
	employee = employeeDataXml.createElement('Employee')
	root.appendChild(employee)
	attributeList = ['firstName', 'lastName', 'hourlyWage', 'hoursWorked']
	employeeValues = [firstName, lastName, hourlyWage, hoursWorked]
	for i in xrange(0, 4):
		child = employeeDataXml.createElement(attributeList[i].title())
		employee.appendChild(child)
		childValue = employeeDataXml.createTextNode(str(employeeValues[i]).lower())
		child.appendChild(childValue)
	employeeDataFile = open('employeeData.xml', 'w')
	root.writexml(employeeDataFile)
	employeeDataFile.close()
	employeeDataXml.unlink()

def updateEmployee(self, firstName, lastName)
ujj

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

	# def setEmployee(self, firstName, lastName, hourlyWage, hoursWorked):
	# 	"""Assign values to employee attributes."""
	# 	self.firstName = firstName.lower()
	# 	self.lastName = lastName.lower()
	# 	self.hourlyWage = str(float(hourlyWage))
	# 	self.hoursWorked = str(float(hoursWorked))

	# def employeeToXML(self):
	# 	"""For testing"""
	# 	doc = minidom.Document()
	# 	root = doc.createElement('Employees')
	# 	doc.appendChild(root)
	# 	""" Need 'Employee' child """
	# 	list = ['firstName', 'lastName', 'hourlyWage', 'hoursWorked']
	# 	for each in list:
	# 		child = doc.createElement(each.title())
	# 		root.appendChild(child)
	# 		childValue = doc.createTextNode(getattr(self,each))
	# 		child.appendChild(childValue)
	# 	f = open('employeeData.xml', 'w')
	# 	root.writexml(f)
	# 	f.close()

	def employeeImport(self, firstName, lastName):
		"""Parses XML and stores selected employee info in employee object."""
		employeeDataXml = minidom.parse('employeeData.xml')
		employees = employeeDataXml.getElementsByTagName('Employee')
		for employee in employees:
			firstNameNode = employee.getElementsByTagName('Firstname')[0].childNodes
			lastNameNode = employee.getElementsByTagName('Lastname')[0].childNodes
			if firstNameNode[0].data == firstName.lower() and lastNameNode[0].data == lastName.lower():
				self.firstName 	 = firstName.lower()
				self.lastName  	 = lastName.lower()
				self.hourlyWage  = float(employee.getElementsByTagName('Hourlywage')[0].childNodes[0].data)
				self.hoursWorked = float(employee.getElementsByTagName('Hoursworked')[0].childNodes[0].data)
				employeeDataXml.unlink()
				return True
		return False

	def printEmployeeReport(self):
		"""Displays employee payroll information."""
		print '%-6s%16s%16s%13s' % \
			('-' * 4, '-' * 11, '-' * 12, '-' * 9)
		print '%-6s%16s%16s%13s' % \
			('Name', 'Hourly Wage', 'Hours Worked', 'Gross Pay')
		print '%-6s%16s%16s%13s' % \
			('-' * 4, '-' * 11, '-' * 12, '-' * 9)
		if len(self.lastName) > 
		print '%.12s, %.1s%15.2f%16.2f%13.2f' % \
			(self.lastName.title(),
				self.firstName.title(),
				self.hourlyWage,
				self.hoursWorked,
				(self.hourlyWage * self.hoursWorked))


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
