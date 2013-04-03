from patronMod import patron
from bookMod import book
from fileInteraction import *
from menuMod import *

def main():
	while True:
		menuSelection = secondaryMenus(mainMenu())
		if menuSelection[1] == 'patron':
			patronMenu(menuSelection)

main()