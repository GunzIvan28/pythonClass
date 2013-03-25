"""
Program: Value to Decimal
Author: Bill Minear

Notes:
	+) Not entirely sure I interpreted
		this assignment correctly.
"""
import os 

# The assignment says to create a dictionary of the values 1-F.
# I'm not sure why it's necessary to have 1-9 in the dictionary.
# Instead, if the value's not in the dictionary (AKA not a letter)
# I just converted it to int and used it directly.
#
# Again, I might have misunderstood what the assignment's trying to do.
conversionDictionary = {'A':10,'B':11,'C':12,'D':12,'E':14,'F':15}

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt'])

def repToDecimal(value, base):
	"""Converts values to decimal."""
	convertedTotal = 0
	exponent = len(value) - 1
	for digit in value:
		try:
			digit = int(digit)
		except ValueError:
			if digit.upper() in conversionDictionary:
				digit = conversionDictionary[digit.upper()]
			else:
				print digit, 'is not a valid value.'
				raw_input('Press ENTER to exit.')
				exit()
		convertedValue = digit * base ** exponent
		convertedTotal = convertedTotal + convertedValue
		exponent = exponent - 1
	print "The integer value is", convertedTotal
	raw_input('Press ENTER to exit.')
	exit()

def main():
	while True:
		clearScreen()
		value = raw_input('Enter a value: ')
		try:
			base = input('Enter the base: ')
			break
		except NameError:
			print '\nBase must be numerical.'
			raw_input('\nPress ENTER to try again.')
	repToDecimal(value, base)

main()