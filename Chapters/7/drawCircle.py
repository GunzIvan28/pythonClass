from math import pi
import turtle
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt']) 

def drawCircle(myTurtle, startingPoint, radius):
	move = 2.0 * pi * radius / 120.0
	myTurtle.up()
	myTurtle.setpos(startingPoint[0], startingPoint[1])
	myTurtle.down()
	for count in xrange(120):
		myTurtle.forward(move)
		myTurtle.setheading(3)
	myTurtle.mainloop()



def main():
	clearScreen()
	while True:
		try:
			xAxis = input('X axis starting point: ')
			yAxis = input('Y axis starting point: ')
			radius = input('Enter the radius: ')
			startingPoint = [xAxis, yAxis]
			break
		except NameError:
			print '\nInput must be numerical.'
			raw_input('Press ENTER to try again.')
	myTurtle = turtle
	drawCircle(myTurtle, startingPoint, radius)

main()