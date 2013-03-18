"""
Program: Value to Decimal
Author: Bill Minear
"""

conversionDictionary = {'A':10,'B':11,'C':12,'D':12,'E':14,'F':15}

def repToDecimal(base, value):
	convertedTotal = 0
	# Exponent is -1 for shifting to index 0.
	exponent = len(value) - 1
	for digit in value:
		if str(digit.upper()) in conversionDictionary:
			digit = conversionDictionary[digit.upper()]
		convertedValue = int(digit) * int(base) ** exponent
		convertedTotal = convertedTotal + convertedValue
		exponent = exponent - 1
	print "The integer value is", convertedTotal

while True:
	value = raw_input('Enter a number: ')
	base = raw_input('Enter the base: ')
	repToDecimal(base, value)