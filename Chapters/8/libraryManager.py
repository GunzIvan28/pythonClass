from patronMod import patron
from bookMod import book
from fileInteraction import *
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt'])

def mainMenu():
	while True:
		clearScreen()
		print 'Welcome to the Book Manager!'
		print 'Please make a selection:'
		print '1) Patron tasks'
		print '2) Book tasks'
		print '3) Exit'
		mainMenuSelection = raw_input('--> ')
		try:
			if int(mainMenuSelection) < 1 or int(mainMenuSelection) > 3:
				raw_input('\nInvalid menu selection. Press ENTER to try again.')
			else:
				return int(mainMenuSelection)
		except ValueError:
			raw_input('\nSelection not numeric. Press ENTER to try again.')

def secondaryMenus(mainMenuSelection):
	if mainMenuSelection == 1:
		clearScreen()
		print 'Patron tasks:'
		print '1) View patron status'
		print '2) Add patron'
		print '3) Remove patron'
		print '4) Exit'
		secMenuSelection = raw_input('--> ')

	elif mainMenuSelection == 2:
		clearScreen()
		print 'Book tasks:'
		print '1) View book status'
		print '2) Book return'
		print '3) Add book'
		print '4) Remove book'
		print '5) Exit'
		secMenuSelection = raw_input('--> ')

	elif mainMenuSelection == 3:
		clearScreen()
		exit()

def main():
	secondaryMenus(mainMenu())


main()	