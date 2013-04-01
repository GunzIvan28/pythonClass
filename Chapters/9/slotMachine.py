from Tkinter import *
import random

class ButtonDemo(Frame):

	def __init__(self):
		Frame.__init__(self)
		self.master.title('Label Demo')
		self.grid()
		self._button = Button(self,
								text = "Click Me",
								command = self._switch)
		self._button.grid(row = 2, column = 1)

	def _getRandPic(self):
		imageDictionary = {0:'cat.gif', 1:'guy.gif', 2:'earth.gif'}
		randImage = imageDictionary[random.randrange(0,3)]
		return randImage


	def _switch(self):
		self._imageDictionary = {0:'cat.gif', 1:'guy.gif', 2:'earthImage.gif'}
		self._randImage1 = PhotoImage(file = self._getRandPic())
		self._randImage2 = PhotoImage(file = self._getRandPic())
		self._randImage3 = PhotoImage(file = self._getRandPic())
		self._catLabel = Label(self, image = self._randImage1)
		self._catLabel.grid(row = 1, column = 0)
		self._guyLabel = Label(self, image = self._randImage2)
		self._guyLabel.grid(row = 1, column = 1)
		self._earthLabel = Label(self, image = self._randImage3)
		self._earthLabel.grid(row = 1, column = 2)

def main():
	ButtonDemo().mainloop()

main()