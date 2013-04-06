"""
Program: Book Manager
Author: Bill Minear

Notes:
	+) Poorly named variables, overly complex,
		could have used better data formatting
		and manipulation, and likely full of bugs.
	+) Didn't occur to me until half way through
		completion that the assignment calls for a
		library class that manipulates the book and
		patron classes. Not sure how I missed that.
		Having that class would have made things easier
		in some ways but I decided not to rewrite.
		+) menuMod provides the functionality that
			the library class would have in a slightly
			different way. Mostly in that it provides
			interaction, whereas the library class
			would have just provided the means to
			interaction.
	+) Lots of functionality that I would like to have
		added. Lots of things I would like to refactor/rewrite.
		Ran out of time.
"""

from menuMod import *

def main():
	while True:
		menuSelection = secondaryMenus(mainMenu())
		if menuSelection[1] == 'patron':
			patronMenu(menuSelection)
		elif menuSelection[1] == 'book':
			bookMenu(menuSelection)

main()