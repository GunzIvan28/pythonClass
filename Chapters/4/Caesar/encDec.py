#!/usr/bin/python
"""
Program: File Encrypt and Decrypt
Author: Bill Minear

Purpose:
	+) Encrypts and decrypts the contents
		of a given file using the Caesar
		Cipher.

Notes:
	-) Program does not handle new lines in
		the file well. New lines are converted
		just as any other character would be and
		are not converted back to new lines
		during decryption.
"""
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt'])

def mainMenu():
	"""Action selection."""
	while True:
		clearScreen()
		print 'What would you like to do?'
		print '1.) Encrypt message'
		print '2.) Decrypt message'
		print '3.) Exit'
		mainMenuAnswer = raw_input('--> ')
		try:
			if int(mainMenuAnswer) <  1 or int(mainMenuAnswer) > 3:
				raw_input('Invalid selection. Press ENTER to try again.')
			else:
				# Return value maybe needs to be an integer?
				return int(mainMenuAnswer)
		except ValueError:
			raw_input('Invalid input. Press ENTER to try again.')

def encrypt(fileName, cipherDistance):
	"""Opens file, encrypts contents, writes back to file."""
	if '.txt' not in fileName:
		fileName = fileName + '.txt'
	try:
		fileToEncrypt = open(fileName, 'r')
		plainText = fileToEncrypt.read()
		fileToEncrypt.close()
		code = ''
		for eachCharacter in plainText:
			ordValue = ord(eachCharacter)
			cipherValue = ordValue + cipherDistance
			if cipherValue > ord('~'):
				cipherValue = ord(' ') + cipherDistance - \
				(ord('~') - ordValue + 1)
			code += chr(cipherValue)
		fileToEncrypt = open(fileName, 'w')
		fileToEncrypt.write(code)
		fileToEncrypt.close()
		print '\nFile encrypted.\n'
		print code
		raw_input('\nPress ENTER to continue.')
	except IOError:
		raw_input('\nUnable to open file. Press ENTER to return to the main menu.')

def decrypt(fileName, cipherDistance):
	"""Opens file, decrypts contents, writes back to file."""
	if '.txt' not in fileName:
		fileName = fileName + '.txt'
	try:
		fileToDecrypt = open(fileName, 'r')
		code = fileToDecrypt.read()
		fileToDecrypt.close()
		plainText = ''	
		for eachCharacter in code:
			ordValue = ord(eachCharacter)
			cipherValue = ordValue - cipherDistance
			if cipherValue < ord(' '):
				cipherValue = ord('~') - \
				(cipherDistance - (ord(' ') - ordValue + 1))
			plainText += chr(cipherValue)
		fileToDecrypt = open(fileName, 'w')
		fileToDecrypt.write(plainText)
		fileToDecrypt.close()
		print '\nFile decrypted.\n'
		print plainText
		raw_input('\nPress ENTER to continue.')
	except IOError:
		raw_input('\nUnable to open file. Press ENTER to return to the main menu.')

def main(mainMenuAnswer):
	"""Actions based on mainMenu()"""

	if mainMenuAnswer == 1:
		"""Encryption"""
		clearScreen()
		fileName = raw_input('Input file to be encrypted: ')
		while True:
			cipherDistance = raw_input('Enter the cipher distance: ')
			try:
				cipherDistance = int(cipherDistance)
				break
			except ValueError:
				raw_input('\nDistance must be numerical. Press ENTER to try again.')
		encrypt(fileName, cipherDistance)

	if mainMenuAnswer == 2:
		"""Decryption"""
		clearScreen()
		fileName = raw_input('Input file to be decrypted: ')
		while True:
			cipherDistance = raw_input('Enter the cipher distance: ')
			try:
				cipherDistance = int(cipherDistance)
				break
			except ValueError:
				raw_input('\nDistance must be numerical. Press ENTER to try again.')
		decrypt(fileName, cipherDistance)

	if mainMenuAnswer == 3:
		clearScreen()
		exit()

# Main loop.
while True:
	main(mainMenu())


