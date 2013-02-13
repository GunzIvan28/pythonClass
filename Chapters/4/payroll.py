"""
Employee Module
"""
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
		f = open('test.xml', 'w')
		root.writexml(f)
		f.close()

def 

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
