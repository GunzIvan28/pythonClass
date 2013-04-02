from Tkinter import *
from tkMessageBox import showinfo
import random

class slotGUI(Frame):

	def __init__(self):
		Frame.__init__(self)
		self.master.title('Slots!')
		self.grid()
		self._initText = Label(self, text = 'Welcome!')
		self._initText.grid(row = 1, column = 1)
		self._button = Button(self,text = "Play!", command = self._switch)
		self._button.grid(row = 2, column = 1)
		# self._currentAmount = Label(self, text = )

	def _getRandPic(self):
		self._imageDictionary = {0:'grape.gif', 1:'cherry.gif', 2:'seven.gif',
									3:'orange.gif', 4:'bar.gif'}
		self._randImage = self._imageDictionary[random.randrange(0,5)]
		return self._randImage

	def _switch(self):
		for i in xrange(0,3):
			self._myList = []
			self._image = PhotoImage(file = self._getRandPic())
			self._imageLabel = Label(self, image = self._image)
			self._myList.append(self._imageLabel)
			self._myList[i].grid(row = 1, column = i)
		# self._image1 = PhotoImage(file = self._getRandPic())
		# self._image2 = PhotoImage(file = self._getRandPic())
		# self._image3 = PhotoImage(file = self._getRandPic())
		# self._image1Label = Label(self, image = self._image1)
		# self._image1Label.grid(row = 1, column = 0)
		# self._image2Label = Label(self, image = self._image2)
		# self._image2Label.grid(row = 1, column = 1)
		# self._image3Label = Label(self, image = self._image3)
		# self._image3Label.grid(row = 1, column = 2)

def main():
	beginMessage = 'You begin with $100.\nEach bet is $10.'
	showinfo(title = 'Welcome!', message = beginMessage)
	slotGUI().mainloop()

main()