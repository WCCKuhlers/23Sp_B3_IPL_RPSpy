import math
from random import randint
import random
score = 0
start_game = True

#rock = 1
#paper = 2
#scissors = 3

playerAns = str(input("Pick rock,paper or scissors"))
compAns = random.randint(1,3)
while start_game:
    if compAns == 1:
        compAns = "rock"
    if compAns == 2:
        compAns = "paper"
    if compAns == 3:
        compAns = "scissors"
    if playerAns == compAns:
        print("It's A Tie! Play Again!")
        start_game = False
        print("You scored",score)
    if playerAns == "rock" and compAns == "paper":
        print("You Lose! Your Rock Got Covered Take The L!")
        start_game = False
        print("You scored",score)
    if playerAns == "paper" and compAns == "scissors":
        print("You Lose! Your Paper Got Cut Take The L!")
        start_game = False
        print("You scored",score)
    if playerAns == "scissors" and compAns == "rock":
        print("You Lose! Your Scissors Got Crushed Take The L!")
        start_game = False
        print("You scored",score)
    if playerAns == "rock" and compAns == "scissors":
        print("You Won! You Crushed The Opponent's Scissors Take The Win While You Can!")
        score = score +1
        print("Score:",score)
    if playerAns == "paper" and compAns == "rock":
        print("You Won! You Covered The Rock Take The Win While You Can!")
        score = score +1
        print("Score:",score)
    if playerAns == "scissors" and compAns == "paper":
        print("You Won! You Cut The Paper Take The Win While You Can!")
        score = score +1
        print("Score:",score)


