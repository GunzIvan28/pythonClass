from payroll import *
from xml.dom.minidom import *

# impl = getDOMImplementation()
# doc = impl.createDocument(None,'Employees', None)
# doc.writexml('employeeData.xml')

fileCheck()
employee = employee()
employee.setEmployee('bill', 'minear', '8.00', '20.00')
employee.addEmployee()



# dom = parse('employeeData.xml')
# for node in dom.getElementsByTagName('Lastname'):
# 	if node.firstChild.nodeValue == 'bill':
# 		print 'Nice!'
# 	elif node.firstChild.nodeValue == 'saya':
# 		print 'Cool!'
# 	elif node.firstChild.nodeValue == 'minear':
# 		print 'Minear!'
