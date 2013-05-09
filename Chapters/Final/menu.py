import os 

class menu(object):

	def __init__(self):
		self._answer = ''

	def _clearScreen(self): 
		os.system(['clear','cls'][os.name == 'nt'])

	def intro(self):
		self._clearScreen()
		print '\n\tWelcome to Battleship!'


menu = menu()
menu.intro()