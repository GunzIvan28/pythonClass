from payroll import *
from xml.dom.minidom import *

# impl = getDOMImplementation()
# doc = impl.createDocument(None,'Employees', None)
# doc.writexml('employeeData.xml')

fileCheck()
employee = employee()
firstName = raw_input('First name: ')
lastName = raw_input('Last name: ')
employeeCheck(firstName, lastName)



# dom = parse('employeeData.xml')
# for node in dom.getElementsByTagName('Lastname'):
# 	if node.firstChild.nodeValue == 'bill':
# 		print 'Nice!'
# 	elif node.firstChild.nodeValue == 'saya':
# 		print 'Cool!'
# 	elif node.firstChild.nodeValue == 'minear':
# 		print 'Minear!'
