# Tic Tac Toe
# Importing important stuff
import os
import random

# Defining global variables
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
p1 = 'X'
p2 = 'O'

# Function to clear screen
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the board
def pB():
  cls()
  print board[0] + '  | ' + board[1] + ' |  ' + board[2]
  print '   |   |   '
  print '-----------'
  print '   |   |   '
  print board[3] + '  | ' + board[4] + ' |  ' + board[5]
  print '   |   |   '
  print '-----------'
  print '   |   |   '
  print board[6] + '  | ' + board[7] + ' |  ' + board[8]

pB()
