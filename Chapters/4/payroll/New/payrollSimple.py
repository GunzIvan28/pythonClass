#!/usr/bin/python

"""
Program: Simple Payroll Program
Author: Bill Minear

Purpose:
	+) Reads and displays payroll
		information from a file. 

Notes:
	+) File must be in format:
		'lastname wage hours'
		+) Must be separated by spaces.
	+) Program only reads .txt files
		and if .txt is not in the file name
		given, the program will append it.
"""
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt']) 

# Inputs filename and opens for read.
while True:
	clearScreen()
	fileName = raw_input('Enter filename or type exit to quit: ')
	if fileName.lower() == 'exit':
		clearScreen()
		exit()
	if '.txt' not in fileName:
		fileName = fileName + '.txt'
	try:
		employeeDataFile = open(fileName, 'r')
		break
	except IOError:
		raw_input('\nUnable to open file. Press ENTER to try again.')

# Outputs data in tabular format.
clearScreen()
print '%-12s%7s%7s' % \
	('Name', 'Hours', 'Pay')
print '%-12s%7s%7s' % \
	('-' * 4, '-' * 5, '-' * 3)
for line in employeeDataFile:
	line = line.split()
	if len(line[0]) < 12:
		line[0] = line[0] + (' ' * (12 - len(line[0])))
	grossPay = float(line[1]) * float(line[2])
	print '%-.12s%7.2f%10.2f' % \
		(line[0].title(), float(line[2]), float(grossPay))
employeeDataFile.close()
raw_input('\nPress ENTER to exit.')
clearScreen()