"""
Program: Password Hash Cracker
Author: Bill Minear (Borrowed from example assignment.)

Notes:
	+) Not sure if my counter operates the way I'd like
		it to because it's being modified in a different
		namespace. This only effects the program ending.
		You could check the file for three separate hashes
		and end it yourself.
	+) The program outputs cracked hash info to a file
		stored in the same directory as the program.
		For whatever reason, the same two hashes are
		output to the file over and over again as the
		program runs. Seems to be a bug here. Not sure
		if it's negatively effecting the program, though
		as it seems to continue working as intended.
	+) Was unable to crack the last hash. "drink" and
		"your" happen pretty quickly. The program was
		working on 7 letter passwords overnight when
		Windows Update decided it was time to reboot.
		But, *ahem* through the use of a word list, I
		was able to determine that the last password
		is "ovaltine".
"""
import md5
import time

counter = 0
localtime = str(time.asctime(time.localtime(time.time())))
hash1 = '0b18a3d7b9c43ff1750d2baa4606b8d0'
hash2 = '62cc0b4ebb0b57b40778179234246c38'
hash3 = '17c0f75d610ec414e5c9be1a6059b65a'

letters = []
for num in xrange(97, 123):
	letters.append(chr(num))

def outputToFile(theHash, password, localtime, counter):
	"""Outputs cracked hash info to a file stored in the same directory as the program."""
	hashFile = open('crackedHashes.txt', 'a')
	hashFile.write('\n\nHash: ' + str(theHash))
	hashFile.write('\nPassword: ' + str(password))
	hashFile.write('\nTime of crack: ' + localtime)
	hashFile.close()
	counter += 1

def hashCheck(password, counter):
	"""Checks for matching hashes."""
	m = md5.new(password)
	if counter > 3:
		exit()
	if (m.hexdigest() == hash1):
		outputToFile(hash1, password, localtime, counter)
	elif (m.hexdigest() == hash2):
		outputToFile(hash2, password, localtime, counter)
	elif (m.hexdigest() == hash3):
		outputToFile(hash3, password, localtime, counter)

def hashCreation(width, position, testPass, counter):
	"""Creates hashes and passes them to hashCheck."""
	# print 'Checking password:', testPass
	for char in letters:
		if (position < width - 1):
			hashCreation(width, position + 1, testPass + char, counter)
		hashCheck(testPass + char, counter)

def main(myNum):
	"""Flow control."""
	hashFile = open('crackedHashes.txt', 'w')
	hashFile.write('Starting at: ' + localtime)
	hashFile.close()
	maxChars = myNum 
	for value in range(0, maxChars + 2):
		hashCreation(value, 0, "", counter)
