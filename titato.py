# Tic Tac Toe
# Importing important stuff
import os
import random
import sys

# Defining global variables
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
p1 = 'X'
p2 = 'O'
turns = 0

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

# Function for if/when someone wins
def win(plyer):
  print '%s WINS!' % plyer
  sys.exit(0)

# Function to check for winner
def check_win(player):
  if board[0]==player and board[1]==player and board[2]==player:
    win(player)
  elif board[3]==player and board[4]==player and board[5]==player:
    win(player)
  elif baord[6]==player and board[7]==player and board[8]==player:
    win(player)
  elif board[0]==player and board[3]==player and board[6]==player:
    win(player)
  elif board[1]==player and board[4]==player and board[7]==player:
    win(player)
  elif board[2]==player and board[5]==player and board[8]==player:
    win(player)
  elif board[0]==player and board[4]==player and board[8]==player:
    win(player)
  elif board[2]==player and board[4]==player and board[6]==player:
    win(player)
  else:
    turns += 1

# Turn function
def turn(playr):
  pB()
  # A bool to tell program if someone picked correct space
  cS = False
  while cS = False:
    try:
      s = int(raw_input('Pick a space (1-9): ')) - 1
      cS = True
    except:
      print 'There was an error!'
    
  # A bool to tell program someone picked correct space again
  cSA = False
  while cSA == False:
    if board[s] == ' ':
      board[s] = playr
      cSA = True
    else:
      print 'That spot is already taken!'

# Main loop:
while turns < 9:
  turn(p1)
  check_win(p1)
  turn(p2)
  check_win(p2)
