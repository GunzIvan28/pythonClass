from Tkinter import *
from tkMessageBox import showinfo
import random

"""
Image scoring:
	1.) Cherry
	2.) Seven
	3.) Bar
	4.) Double Bar
	5.) Triple Bar

	+) Any instance of 1
		+) self._money += 2
	+) Any combo of 0, 2, 4
		+) self._money += 10
	+) All 0
		+) self._money += 30
	+) All 2
		+) self._money += 60
	+) All 4
		+) self._money += 120
	+) All 3
		+) self._money += 200
	+) Else
		+) self._money -= 5


"""
class slotGUI(Frame):

	def __init__(self):
		Frame.__init__(self)
		self.master.title('Slots!')
		self.grid()
		self._money = 100
		self._imageDictionary = {0:'bar.gif', 1:'cherry.gif', 2:'doubleBar.gif',
									3:'seven.gif', 4:'tripleBar.gif'}
		self._imageList = []
		self._initText = Label(self, text = 'Welcome!', height = 5, width = 20, font = 16)
		self._initText.grid(row = 1, column = 1)
		self._button = Button(self,	text = "Play!", command = self._leverPull)
		self._button.grid(row = 2, column = 1)

	def _getRandPic(self):
		self._randImage = self._imageDictionary[random.randrange(0,5)]
		return self._randImage

	def _payout(self):
		self._payoutCheck = 0
		for key, value in self._imageDictionary.iteritems():
			for image in self._imageList:
				if image == value:
					self._payoutCheck += key % 2
		if self._payoutCheck == 0:
			self._money += 10
		else:
			self._money -= 5

	def _leverPull(self):
		self._labelList = []
		for i in xrange(0,3):
			self._imageList.append(PhotoImage(file = self._getRandPic()))
			self._labelList.append(Label(self, image = self._imageList[i]))
			self._labelList[i].grid(row = 1, column = i)
		self._payout() 
		self._moneyDisplay = Label(self, text = self._money)
		self._moneyDisplay.grid(row = 2, column = 0)

def main():
	beginMessage = 'You begin with $100.\nEach bet is $10.'
	showinfo(title = 'Welcome!', message = beginMessage)
	slotGUI().mainloop()

main()