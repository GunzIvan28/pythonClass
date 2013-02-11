#!/usr/bin/python

test = raw_input('Enter a string: ')
offSet = input('Enter an offset: ')
for thing in test:
	ordValue = ord(thing)
	cipherValue = ordValue + offSet 
	# print 'Cipher Val: ' + str(cipherValue)
	# print ord('z')
	# print ord('a') + offSet
	# print ord('z') - ordValue + 1
	# print chr(ord('a') + offSet - \
	# (ord('z') - ordValue + 1))
	if cipherValue > ord('z'):
		cipherValue = ord('a') + offSet - \
					  (ord('z') - ordValue +1)
	print cipherValue

