
conversionDictionary = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,
						10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def main(base, value):
	convertedValue = 0
	exponent = len(value) - 1
	for digit in value:
		convertedValue = convertedValue + int(digit) * int(base) ** exponent
		exponent = exponent - 1
		
	print "The integer value is", convertedValue 

while True:
	value = raw_input('Enter a number: ')
	base = raw_input('Enter the base: ')
	main(base, value)