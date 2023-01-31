#Rock, Paper, Scissors

import math
from random import randint
import random

#rock = 1
#paper = 2
#scissors = 3

playerAns = str(input("Pick rock, paper, or scissors "))

comAns = random.randint(1,3)

if comAns == 1:
    comAns = "rock"
    print("Computer picked rock!")
    
if comAns == 2:
    comAns = "paper"
    print("Computer picked paper!")
          
if comAns == 3:
    comAns = "scissors"
    print("Computer picked scissors!")    

if comAns == playerAns:
    print("Tie")
if comAns == 'rock' and playerAns == 'paper':
    print(f"Player {playerAns} covers computer {comAns}, YOU WIN!")
if comAns == 'rock' and playerAns == 'scissors':
    print(f"Computer {comAns} destroys players {playerAns}, YOU LOSE!")
if comAns == 'paper' and playerAns == 'rock':
    print(f"Computer {comAns} covers player's {playerAns}, YOU LOSE!")
if comAns == 'paper' and playerAns == 'scissors':
    print(f"Computer {comAns} is cut by player {playerAns}, YOU WIN!")
if comAns == 'scissors' and playerAns == 'rock':
    print(f"Computer {comAns} is broke by player {playerAns}, YOU WIN!")
if comAns == 'scissors' and playerAns == 'paper':
    print(f"Computer {comAns} cuts player {playerAns}, YOU LOSE!")

playerResp = str(input("Would you like to play again? yes or no?"))

if playerResp == 'yes':
    startGame = True
else:
    startGame = False
