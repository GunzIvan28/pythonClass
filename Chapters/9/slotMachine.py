from Tkinter import *
from tkMessageBox import showinfo
import random

class slotGUI(Frame):

	def __init__(self, money):
		Frame.__init__(self)
		self.master.title('Slots!')
		self.grid()
		self._money = 100
		self._initText = Label(self, text = 'Welcome!', height = 5, width = 20, font = 16)
		self._initText.grid(row = 1, column = 1)
		self._button = Button(self,	text = "Play!", command = self._switch)
		self._button.grid(row = 2, column = 1)

	def _getRandPic(self):
		self._imageDictionary = {0:'grape.gif', 1:'cherry.gif', 2:'seven.gif',
									3:'orange.gif', 4:'bar.gif'}
		self._randImage = self._imageDictionary[random.randrange(0,5)]
		return self._randImage

	def _switch(self):
		self._imageList = []
		self._labelList = []
		for i in xrange(0,3):
			self._imageList.append(PhotoImage(file = self._getRandPic()))
			self._labelList.append(Label(self, image = self._imageList[i]))
			self._labelList[i].grid(row = 1, column = i)
		self._money -= 10
		self._moneyDisplay = Label(self, text = self._money)
		self._moneyDisplay.grid(row = 2, column = 0)

def main():
	money = 100
	beginMessage = 'You begin with $100.\nEach bet is $10.'
	showinfo(title = 'Welcome!', message = beginMessage)
	slotGUI(money).mainloop()

main()