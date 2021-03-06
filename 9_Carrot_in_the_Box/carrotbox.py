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
print()
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLD box in front of you.')
print()
print(p1Name + ', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and don\'t look!!!')
input('When ' + p2Name + 'has closed their eyes, press enter...')
print()

print(p1Name + ' here is the inside of your box:')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
    ___VV____
   |   VV    |
   |   VV    |
   |___||____|    __________
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
  (carrot!)''')
    print(playerNames)
else:
    print('''
    _________
   |         |
   |         |
   |_________|    __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   RED   | |  |   GOLD  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/
 (no carrot!)''')
    print(playerNames)

input('Press Enter to continue...')
