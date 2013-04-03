import os
from fileInteraction import *

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt'])

def inputCheck(selectionVar,lower,upper):
	"""Validates input per menu."""
	try:
		if int(selectionVar) < lower or int(selectionVar) > upper:
			return False
		else:
			return int(selectionVar)
	except ValueError:
		return False


def mainMenu():
	while True:
		clearScreen()
		print 'Welcome to the Book Manager!'
		print 'Please make a selection:'
		print '1) Patron tasks'
		print '2) Book tasks'
		print '3) Exit'
		mainMenuSelection = raw_input('--> ')
		menuSelection = inputCheck(mainMenuSelection,1,3)
		if menuSelection == False:
			raw_input('Selection not valid. Press ENTER to try again.')
		else:
			return menuSelection

def secondaryMenus(mainMenuSelection):
	if mainMenuSelection == 1:
		while True:
			clearScreen()
			print 'Patron tasks:'
			print '1) View patron status'
			print '2) Add patron'
			print '3) Remove patron'
			print '4) Return to Main Menu'
			secMenuSelection = raw_input('--> ')
			menuSelection = inputCheck(secMenuSelection,1,4)
			if menuSelection == False:
				raw_input('Selection not valid. Press ENTER to try again.')
			else:
				menuSelection = [menuSelection, 'patron']
				return menuSelection

	elif mainMenuSelection == 2:
		while True:
			clearScreen()
			print 'Book tasks:'
			print '1) View book status'
			print '2) Book return'
			print '3) Add book'
			print '4) Remove book'
			print '5) Return to Main Menu'
			secMenuSelection = raw_input('--> ')
			menuSelection = inputCheck(secMenuSelection,1,5)
			if menuSelection == False:
				raw_input('Selection not valid. Press ENTER to try again.')
			else:
				menuSelection = [menuSelection, 'book']
				return menuSelection

	elif mainMenuSelection == 3:
		clearScreen()
		exit()

def patronMenu(secMenuSelection):
	if secMenuSelection[0] == 1:
		firstName = raw_input("\nEnter Patron's first name: ")
		lastName = raw_input("Enter Patron's last name: ")
		patronInfo = checkForPatron(firstName.lower(),lastName.lower())
		if patronInfo == False:
			raw_input('Patron not found. Press ENTER to continue.')
		else:
			clearScreen()
			print 'Name:', patronInfo[0].capitalize(), patronInfo[1].capitalize()
			print 'Number of books:', patronInfo[2]
			raw_input('\nPress ENTER to continue.')
	if secMenuSelection[0] == 2:
		firstName = raw_input("\nEnter Patron's first name: ")
		lastName = raw_input("Enter Patron's last name: ")
		patronInfo = checkForPatron(firstName.lower(),lastName.lower())
		if patronInfo == False:
			newPatron(firstName.lower(),lastName.lower(),'0')
			raw_input('Patron successfully added. Press ENTER to continue.')
		else:
			raw_input('Patron already exists. Press ENTER to continue.')
	if secMenuSelection[0] == 3:
		firstName = raw_input("Enter Patron's first name: " )
		lastName = raw_input("Enter Patron's last name: ")
		patronInfo = checkForPatron(firstName.lower(),lastName.lower())
		if patronInfo != False:
			removePatron(patronInfo)
			raw_input('Patron successfully removed. Press ENTER to continue.')
		else:
			raw_input('Patron not found. Press ENTER to continue.')









