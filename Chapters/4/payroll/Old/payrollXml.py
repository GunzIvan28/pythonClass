"""
XML interaction for the Payroll program.
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

def addEmployee(newEmployeeValues):
	"""Adds an employee to the XML file."""
	employeeDataXml = minidom.parse('employeeData.xml')
	root = employeeDataXml.documentElement
	employee = employeeDataXml.createElement('Employee')
	root.appendChild(employee)
	attributeList = ['FirstName', 'LastName', 'HourlyWage', 'HoursWorked']
	for i in xrange(0, 4):
		child = employeeDataXml.createElement(attributeList[i])
		employee.appendChild(child)
		childValue = employeeDataXml.createTextNode(str(newEmployeeValues[i]).lower())
		child.appendChild(childValue)
	employeeDataFile = open('employeeData.xml', 'w')
	root.writexml(employeeDataFile)
	employeeDataFile.close()
	employeeDataXml.unlink()

def removeEmployee(employeeName):
	"""Removes an employee from the XML file."""
	employeeDataXml = minidom.parse('employeeData.xml')
	root = employeeDataXml.documentElement
	employees = employeeDataXml.getElementsByTagName('Employee')
	for employee in employees:
		firstNameNode = employee.getElementsByTagName('FirstName')[0].childNodes[0].data
		lastNameNode = employee.getElementsByTagName('LastName')[0].childNodes[0].data
		if firstNameNode == employeeName[0] and lastNameNode == employeeName[1]:
			root.removeChild(employee)
	employeeDataFile = open('employeeData.xml', 'w')
	root.writexml(employeeDataFile)
	employeeDataFile.close()
	employeeDataXml.unlink()

def getEmployeeInfo(employeeName):
	"""Returns all information for an employee."""
	employeeDataXml = minidom.parse('employeeData.xml')
	employees = employeeDataXml.getElementsByTagName('Employee')
	for employee in employees:
		firstNameNode = employee.getElementsByTagName('FirstName')[0].childNodes[0].data
		lastNameNode = employee.getElementsByTagName('LastName')[0].childNodes[0].data
		if firstNameNode == employeeName[0] and lastNameNode == employeeName[1]:
			hourlyWage = float(employee.getElementsByTagName('HourlyWage')[0].childNodes[0].data)
			hoursWorked = float(employee.getElementsByTagName('HoursWorked')[0].childNodes[0].data)
			employeeInfo = [employeeName[0], employeeName[1], hourlyWage, hoursWorked]
			return employeeInfo

def updateEmployee(employeeInfo):
	employeeDataXml = minidom.parse('employeeData.xml')
	employees = employeeDataXml.getElementsByTagName('Employee')
	for employee in employees:
		firstNameNode = employee.getElementsByTagName('FirstName')[0].childNodes[0].data
		lastNameNode = employee.getElementsByTagName('LastName')[0].childNodes[0].data
	