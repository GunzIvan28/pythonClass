"""
Program: Battleship
Author: Bill Minear

Notes:
	+) First of all, I'm sorry you have to read this code.
		It's a mess. It's confusing. It's poorly commented. 
		The game, when you play it,	is confusing. There are 
		several bugs. It works (most of the time), but it's
		nothing fancy.
	+) Being sick destroyed most of the time I had set aside
		to work on this. It got pushed back and was written
		in two non-stop days of "wtf does that error mean"
		and "this is ugly and overly complex but I don't
		have the time to stop and think about doing it better".
	+) The computer opponent does not randomly place their ships.
		I know this was a requirement for the final and it also
		means the game is not worth playing more than once (if
		you pick up on it). I added static positions as a means of
		testing throughout development and didn't realize until
		recently that I forgot to implement random fleet placement.
		Just going to have to take a hit on that one (no pun intended).
"""
from players import player
from board import gameboard
from menus import menu

# Boards
humanBoard = gameboard()
hitBoard = gameboard()

# Players
human = player(0)
computer = player(1)

# Interaction object. 
menu = menu()

# Intro and placement instructions
menu.intro()
menu.placementInst()

# Setting fleet.
human.storeShips(menu.placeShips(humanBoard))

# Main game and instructions
menu.mainInst()
menu.mainGame(human, computer, humanBoard, hitBoard)

