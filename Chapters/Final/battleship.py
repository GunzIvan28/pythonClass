from players import player
from board import gameboard
from menus import menu

# Boards
myBoard = gameboard()
hitBoard = gameboard()

# Players
human = player(0)
computer = player(1)

# Game interaction.
menu = menu()

# Instructions and intro
menu.intro()
menu.placementInst()

# Setting fleet.
human.storeShips(menu.placeShips(myBoard))

# Check for hit.
myBoard.placeMarker(human.checkHit('A1'))

# Display boards.
hitBoard.display()
myBoard.display()
