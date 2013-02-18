"""
Employee Module


Where do I check to see if the xml file exists?
"""
from os.path import exists
from xml.dom import minidom

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

	def employeeCheck(self, firstName, lastName):	
		employeeData = open('employeeData.xml', 'r')
		xml = minidom.parse(employeeData)

	def addEmployee(self):
		employeeDataXml = minidom.parse('employeeData.xml')
		root = employeeDataXml.documentElement
		employee = employeeDataXml.createElement('Employee')
		root.appendChild(employee)
		list = ['firstName', 'lastName', 'hourlyWage', 'hoursWorked']
		for each in list:
			child = employeeDataXml.createElement(each.title())
			employee.appendChild(child)
			childValue = employeeDataXml.createTextNode(str(getattr(self,each)))
			child.appendChild(childValue)
		employeeDataFile = open('employeeData.xml', 'w')
		root.writexml(employeeDataFile)
		employeeDataFile.close()
		root.unlink()






def fileCheck():
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
