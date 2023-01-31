# Ben Smith LNBenRPS  for rock, Paper, Scissors
import math
from random import randint
import random
rock = 1
papaer = 2
scissors = 3
playerAns = str(input("pick rock, paper, or scissors"))
comAns = random.randint(1,3)

if comAns ==1: # condition
    comAns = "rock" #TRUE
if comAns == 2: # condition
    comAns ="paper" # TRUE
if comAns == 3: # condition
    comAns ="scissors" #TRUE
        
if comAns == playerAns:
    print("player won")
if comAns == "rock" and playerAns == "paper":
    print("Player ", playerAns, "covers computer ", comAns, "PlayerWins")
if comAns == "rock" and playerAns == "rock":
    print ("computer won")
if comAns == ("paper" and playerAns == "scissors"):
    print("player won")
if comAns == "scissors" and playerAns == "rock":
    print("player won")
if comAns == ("scissors" and playerAns == "paper"):
   
    print("computer", comAns, " cuts", playerAns, ": Computer Wins")
