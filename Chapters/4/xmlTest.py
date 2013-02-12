from xml.dom import minidom
from payroll import *

employee = employee()
employee.setEmployee('bill', 'minear', '8.00', '20.00')
employee.employeeToXML()

