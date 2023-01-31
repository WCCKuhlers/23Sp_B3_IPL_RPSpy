import math
from random import randint
import random

#rock = 1
#paper = 2
#scissors = 3

playerAns = str(input("Pick rock, paper, or scissors"))
compAns = random.randint(1,3)

if compAns == 1:
    compAns = "rock"
if compAns == 2:
    compAns = "paper"
if compAns == 3:
    compAns = "scissors"
if playerAns == compAns:
    print("It's a Tie! Play again!")
if playerAns == "rock" and compAns == "paper":
    print("Your rock got covered! You lose! Common L ngl")
if playerAns == "paper" and compAns == "scissors":
    print("Your paper got cut! You lose! Common L ngl")
if playerAns == "scissors" and compAns == "rock":
    print("Your scissors got crushed! You lose! Common L ngl")
if playerAns == "rock" and compAns == "scissors":
    print("You crushed the Opponent's scissors! You won! That was easy difficulty though.")
if playerAns == "paper" and compAns == "rock":
    print("You covered the Opponent's rock! You won! That was easy difficulty though.")
if playerAns == "scissors" and compAns == "paper":
    print("You cut the Opponent's paper! You won! That was easy difficulty though.")
