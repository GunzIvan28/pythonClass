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
	hashFile = open('crackedHashes.txt', 'a')
	hashFile.write('\n\nHash: ' + str(theHash))
	hashFile.write('\nPassword: ' + str(password))
	hashFile.write('\nTime of crack: ' + localtime)
	hashFile.close()
	counter += 1

def hashCheck(password, counter):
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
	print 'Checking password:', testPass
	for char in letters:
		if (position < width - 1):
			hashCreation(width, position + 1, testPass + char, counter)
		hashCheck(testPass + char, counter)

def main():
	hashFile = open('crackedHashes.txt', 'w')
	hashFile.write('Starting at: ' + localtime)
	hashFile.close()
	maxChars = 8
	for value in range(1, maxChars + 1):
		hashCreation(value, 0, "", counter)

main()