"""Carrot in a box, by Al Sweigart al@inventwithpython.com
A silly bluffing game between two human players."""

import random

print('''Carrot in a box, by Al Sweigart al@inventwithpython.com

This is a bluffing game for 2 human players. Each player has a box.
One box has a carrot in it. To win, you mush have the box with the carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot in my box"
or "There is no carrot in my box". The second player then gets to decide of the want to swap 
boxes or not.
''')

input('Please enter to begin....')

p1Name = input("Human player 1, enter your name: ")
p2Name = input("Human player 2, enter your name: ")
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''HERE ARE 2 BOXES:
   __________    __________
  /         /|  /         /|
 +---------+ | +---------+ |
 |   RED   | | |   GOLD  | |
 |   BOX   | / |   BOX   | /
 +---------+/  +---------+/''')

print()
print(playerNames)