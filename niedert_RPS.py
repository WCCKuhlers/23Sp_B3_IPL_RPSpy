import math
from random import randint
import random
start_game = true
#rock = 1
#paper = 2
#scissors = 3
# 1 = sign is assighning 2 = is comparing

score = 0


playerAns = str(input("rock, paper or scissors!!! ")) #STR OR STRING IS A TEXT
comAns = random.randint(1,3)

if comAns == 1: #condition
    comAns = "rock"

if comAns == 2:
    comAns = "paper"

if comAns == 3:
    comAns = "scissors"

if comAns == playerAns:
    print ("tie!")
while start_game:
    if comAns == "rock" and playerAns == "paper":
        print ("Player Won")
        print ("paper covered rock! ")
        score = score + 1
        print ("player score is", score,)
    if comAns == "paper" and playerAns == "scissors":
        print ("Player Won")
        print ("scissors cuts paper ")
        score = score + 1
        print ("player score is", score,)
    if comAns == "scissors" and playerAns == "rock":
        print (" PLayer Won! ")
        print ("rock crushes scissors ")
        score = score + 1
        print ("player score is", score,)
    if playerAns == "paper" and comAns == "scissors":
        print ("Player lost :[ ")
        print ("scissors cut paper! ")
        score = score - 1
        print ("player score is", score,)
    if playerAns == "scissors" and comAns == "rock":
        print ("Player lost :[ ")
        print ("rock crushes scissors ")
        score = score - 1
        print ("player score is", score,)
    if playerAns == "rock" and playerAns == "paper":
        print ("Player lost :[ ")
        print ("paper covered rock ")
        score = score - 1
        print ("player score is", score,)

if score == - 1
    print ("you've lost too many times")
    start_game = False
    
