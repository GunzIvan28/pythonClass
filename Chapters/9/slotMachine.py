from Tkinter import *
from tkMessageBox import showinfo
import random

class slotGUI(Frame):

	def __init__(self):
		Frame.__init__(self)
		self.master.title('Slots!')
		self.grid()
		self._initText = Label(self, text = 100)
		self._initText.grid(row = 1, column = 1)
		self._button = Button(self,text = "Play!", command = self._switch)
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
		self._currentAmount = Label(self, text = '100')
		self._myMoney = IntVar()
		if self._myMoney == 0:
			self._moneyActual = 90
			self._myMoney.set(self._moneyActual)
		else:
			self._moneyActual -= 10
			self._myMoney.set(self._moneyActual)
		self._currentAmount = Label(self, textvariable = self._myMoney)
		self._currentAmount.grid(row = 2, column = 0)

def main():
	beginMessage = 'You begin with $100.\nEach bet is $10.'
	showinfo(title = 'Welcome!', message = beginMessage)
	slotGUI().mainloop()

main()