




def mainMenu():
	"""Action selection."""
	print 'What would you like to do?'
	print '1.) Encrypt message.'
	print '2.) Decrypt message.'
	print '3.) Exit'
	mainMenuAnswer = raw_input('--> ')
	try:
		if int(mainMenuAnswer) <  1 or int(mainMenuAnswer) > 3:
			raw_input('Invalid selection. Press ENTER to try again.')
		else:
			# Return value maybe needs to be an integer?
			return mainMenuAnswer
	except ValueError:
		raw_input('Invalid input. Press ENTER to try again.')

def encrypt(fileName, cipherDistance):
	"""Opens file, encrypts contents, and writes it back to the file."""
	try:
		fileToEncrypt = open(fileName, 'w')
	except IOError:
		raw_input('Unable to open file. Press ENTER to return to the main menu.')
	for eachCharacter in fileToEncrypt:
		ordValue = ord(eachCharacter)
		cipherValue = ordValue + distance
		if cipherValue > ord('z'):
			cipherValue = ord('a') + distance - \
			(ord('z') - ordValue + 1)
		code += chr(cipherValue)
	fileToEncrypt.write(code)
	fileToEncrypt.close()
	return 'File encrypted!'


def main(mainMenuAnswer):
	"""Actions based on mainMenu()"""

	if mainMenuAnswer == 1:
		fileName = raw_input('Input file to be encrypted: ')
		while True:
			cipherDistance = raw_input('Enter the cipher distance: ')
			try:
				cipherDistance = int(cipherDistance)
			except ValueError:
				raw_input('Distance must be numerical. Press ENTER to try again.')
		print encrypt(fileName, cipherDistance)


	# if mainMenuAnswer == 2:

	if mainMenuAnswer == 3:
		exit()




while True:
	main(mainMenu)


