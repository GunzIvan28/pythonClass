from menuMod import *

def main():
	while True:
		menuSelection = secondaryMenus(mainMenu())
		if menuSelection[1] == 'patron':
			patronMenu(menuSelection)
		elif menuSelection[1] == 'book':
			bookMenu(menuSelection)

main()