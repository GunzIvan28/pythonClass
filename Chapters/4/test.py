#!/usr/bin/python

print '1.) Add employee'
print '2.) Print employee info'
answer = input('--> ')

if answer == 1:
	employeeName = raw_input('Employee Name: ')
	hourlyWage = raw_input('Hourly Wage: ')
	hoursWorked = raw_input('Hours Worked: ')
	employeeInfo = []
	fileLine = ' '.join(employeeName, hourlyWage, hoursWorked)
	print fileLine
	# f = open('myfile.txt', 'r')
	# for line in f:
	# 	print line
	# f.close)(
# elif answer == 2:
# 	input = raw_input('Write what:\n')
# 	f = open('myfile.txt', 'a')
# 	f.write(input)
# 	f.close()


# test = raw_input('Enter a string: ')
# offSet = input('Enter an offset: ')
# for thing in test:
# 	ordValue = ord(thing)
# 	cipherValue = ordValue + offSet 
# 	# print 'Cipher Val: ' + str(cipherValue)
# 	# print ord('z')
# 	# print ord('a') + offSet
# 	# print ord('z') - ordValue + 1
# 	# print chr(ord('a') + offSet - \
# 	# (ord('z') - ordValue + 1))
# 	if cipherValue > ord('z'):
# 		cipherValue = ord('a') + offSet - \
# 					  (ord('z') - ordValue +1)
# 	print cipherValue

# ASCII 32 through 126
# 	if Greater than 126 do:
# 		fancy math that loops back around