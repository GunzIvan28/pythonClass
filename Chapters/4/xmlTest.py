# from payroll import *
# from xml.dom.minidom import *
from menus import *
from payrollXml import *

doesFileExist = fileCheck()
if doesFileExist == 0:
	pass
elif doesFileExist == 1:
	raw_input('File could not be created.')
elif doesFileExist == 2:
	raw_input('File could not be written to.')

test(getEmployeeName())
# addEmployee(newEmployee())

# impl = getDOMImplementation()
# doc = impl.createDocument(None,'Employees', None)
# doc.writexml('employeeData.xml')

# def test(test1, test2):
# 	testLocals = locals()
# 	for local in testLocals:
# 		print local

# test('test1', 'test2')


# fileCheck()
# employee = employee()
# firstName = raw_input('First name: ')
# lastName = raw_input('Last name: ')
# test = employee.employeeImport(firstName, lastName)
# if test == True:
# 	print employee
# else:
# 	print 'False'

# dom = parse('employeeData.xml')
# for node in dom.getElementsByTagName('Lastname'):
# 	if node.firstChild.nodeValue == 'bill':
# 		print 'Nice!'
# 	elif node.firstChild.nodeValue == 'saya':
# 		print 'Cool!'
# 	elif node.firstChild.nodeValue == 'minear':
# 		print 'Minear!'
