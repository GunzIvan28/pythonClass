"""
Program: TKinter Slot Machine
Author: Bill Minear

Notes:
	+) Very rudimentary. Wanted to get started
		on the threaded password cracker.
	+) Probably could use a couple more images
		in the loop. Winning happens fairly
		regurlaly, though not enough that
		you'll never lose.
"""


from Tkinter import *
from tkMessageBox import showinfo
import random

class slotGUI(Frame):

	def __init__(self):
		Frame.__init__(self)
		self.master.title('Slots!')
		self.grid()
		self._money = 100
		self._imageDictionary = {0:'bar.gif', 1:'cherry.gif', 2:'doubleBar.gif',
									3:'seven.gif', 4:'tripleBar.gif'}
		self._initText = Label(self, text = 'Welcome!', height = 5, width = 20, font = 16)
		self._initText.grid(row = 1, column = 1)
		self._button = Button(self,	text = "Play!", command = self._leverPull)
		self._button.grid(row = 2, column = 1)

	def _getRandPic(self):
		"""Returns a random image from self._imageDictionary."""
		self._randImage = self._imageDictionary[random.randrange(0,5)]
		return self._randImage

	def _payout(self):
		"""Adjusts money amount."""
		self._sevens = '' 
		if self._money == 0:
			self._noMoneyMessage = "You've run out of money!" 
			showinfo(title = 'No more money!', message = self._noMoneyMessage)
			exit()
		self._payoutCheck = 0
		for image in self._fileNameList:
			for key, value in self._imageDictionary.iteritems():
				if image == value:
					self._sevens = self._sevens + str(key)
					self._payoutCheck += key % 2
		if self._payoutCheck == 0:
			self._money += 10
		elif self._sevens == '333':
			self._money += 100
		else:
			self._money -= 5

	def _leverPull(self):
		"""Updates images and calls _payout to adjust money."""
		self._fileNameList = []
		self._imageList = []
		self._labelList = []
		for i in xrange(0,3):
			self._fileNameList.append(self._getRandPic())
		for i in xrange(0,3):
			self._imageList.append(PhotoImage(file = self._fileNameList[i]))
			self._labelList.append(Label(self, image = self._imageList[i]))
			self._labelList[i].grid(row = 1, column = i)
		self._payout() 
		self._moneyFormat = '$' + str(self._money)
		self._moneyDisplay = Label(self, text = self._moneyFormat)
		self._moneyDisplay.grid(row = 2, column = 0)

def main():
	"""Program start."""
	beginMessage = 'You begin with $100.' + \
					'\nEach bet costs $5.' + \
					'\nAny combo of all BARs adds $10.' + \
					'\nAll 7s is a Jackpot and adds $100.'
	showinfo(title = 'Welcome!', message = beginMessage)
	slotGUI().mainloop()

main()