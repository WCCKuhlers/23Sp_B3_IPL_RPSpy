#Rock, paper, Scissors
import math
from random import randint
import random

#rock = 1
#paper = 2
#scissors = 3

playerans = str(input("Pick rock, paper, or scissors"))

comAns = random.randint(1,3)

if comAns == 1:
    comAns = "rock"
if comAns == 2:
    comAns = "paper"
if comAns == 3:
    comAns = "scissors"


if comAns == playerAns:
    print("Tie")
if comAns == 'rock' and playerAns == 'paper':
    print(f"Player {playerAns} covers computer {playerAns}, YOU LOSE!")
if comAns == 'rock' and playerAns == 'scissors':
    print(f"Computer {comAns} destroys players {playerAns}, YOU LOSE!")
if comAns == 'paper' and playerAns == 'rock':
    print(f"Computer {comAns} is cut by player {playerAns}, YOU WIN!")
if comAns == 'paper' and playerAns == 'Scissors':
    print(f"Computer {comAns} is broke by player {playerAns}, YOU WIN!")
if comAns == 'scissors' and playerAns == 'paper':
    print(f"Computer {comAns} cuts player {playerAns}, YOU LOSE!")

#rock = 1
#paper = 2
#scissors = 3

playerans = str(input("Pick rock, paper, or scissors"))

comAns = random.randint(1,3)
if comAns == 1: # conition
    comAns = "rock" # TRUE
if comAns == 2: # condition
    comAns = "paper" # TRUE
if comAns == 3: # condition
    comAns = "scissors" # TRUE

if comAns == playerAns:
    print("Tie")
    
