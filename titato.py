# Tic Tac Toe
# Importing important stuff
import os
import random
import sys
import time

# Defining global variables
turns = 0
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

# Function for if/when someone wins
def win(plyer):
  cls()
  print '*********'
  print '%s WINS!' % plyer
  print '*********'
  time.sleep(1)
  sys.exit(0)

# Function to check for winner
def check_win(player):
  if board[0]==player and board[1]==player and board[2]==player:
    win(player)
  elif board[3]==player and board[4]==player and board[5]==player:
    win(player)
  elif board[6]==player and board[7]==player and board[8]==player:
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

# A little javascript function for my purposes
def prompt(question):
  # A bool to see if there is still help needed
  hN = True
  while hN == True:
    try:
      nS = int(raw_input(str(question))) - 1
      return nS
      hN = False
    except:
      print 'Invalid!'

# Turn function
def turn(playr):
  # A bool to tell program if someone picked correct space
  cS = False
  while cS == False:
    try:
      s = int(raw_input('Pick a space (1-9): ')) - 1
      cS = True
    except:
      print 'That is invalid!'
    
  # A bool to tell program someone picked correct space again
  cSA = False
  while cSA == False:
    try:
      if board[s] == ' ':
        board[s] = playr
        cSA = True
      else:
        print 'Spot taken!'
        pB()
        print ''
        s = prompt('Pick a space (1-9): ')
    except:
      s = prompt('Pick a space (1-9): ')

# Main loop:
while turns < 9:
  pB()
  print ''
  turn(p1)
  turns += 1
  pB()
  print ''
  check_win(p1)
  pB()
  print ''
  turn(p2)
  turns += 1
  pB()
  print ''
  check_win(p2)
