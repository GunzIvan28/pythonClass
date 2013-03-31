"""
Program: drawCircle
Author: Bill Minear

Notes:
	+) Noticed some differences between
		the turtle syntax in the book
		and what I was able to implement.
		+) Not sure if there's a version
			difference or if I've just 
			misinterpreted something.
		+) Mostly used
			http://docs.python.org/2/library/turtle.html
			for syntax and the book for
			flow control.
"""

from math import pi
import turtle
import os 

def clearScreen(): 
    os.system(['clear','cls'][os.name == 'nt']) 

def drawCircle(myTurtle, centerPoint, radius):
	"""Draws circle with turtle object based on inputs	."""
	move = 2.0 * pi * radius / 120.0
	myTurtle.setheading(90) # Orient turtle North.
	myTurtle.up()
	myTurtle.setpos((centerPoint[0] + radius), centerPoint[1]) # Move to circle's right outer edge. 
	myTurtle.down()
	for count in xrange(120):
		myTurtle.forward(move)
		myTurtle.left(3)
	myTurtle.mainloop()

def main():
	"""Program flow control."""
	clearScreen()
	while True:
		try:
			xAxis = input('X axis starting point: ')
			break
		except NameError:
			print '\nInput must be numerical.'
			raw_input('\nPress ENTER to try again.')
	while True:
		try:
			yAxis = input('Y axis starting point: ')
			break
		except NameError:
			print '\nInput must be numerical.'
			raw_input('\nPress ENTER to try again.')
	while True:
		try:
			radius = input('Enter the radius: ')
			centerPoint = [xAxis, yAxis]
			break
		except NameError:
			print '\nInput must be numerical.'
			raw_input('\nPress ENTER to try again.')
	print "\nWe'll now draw the circle."
	print '\nTo exit the program when the circle'
	print 'is complete just close the window.'
	raw_input('\nPress ENTER to continue.')
	myTurtle = turtle
	drawCircle(myTurtle, centerPoint, radius)

main()