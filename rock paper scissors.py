
# rock paper scissors

import random

choices = ["rock" , "paper" , "scissors"]
print("Choices :  Rock , Paper , Scissors or Quit")
print("Rules : - ")
print("Paper covers Rock")
print("Scissor tear Paper")
print("Rock can break a pair of scssors ")
choice = input("Enter your choice :  ")

while choice != "quit":
    choice = choice.lower()
    computer = random.choice(choices)
    if choice == computer: # tie
        print("computer : " , computer)
        print("Its a TIE    : - ) ")
    if  computer == "rock" and choice == "scissors": # rock  scissors
        print("computer : " , computer)
        print("COMPUTER    WINS !!!!!!!!!!!!!!!!!")
    if  computer == "rock" and choice == "paper": # rock paper
        print("computer : " , computer)
        print("YOU    WIN !!!!!!!!!!!!!!!!!")
    if  computer == "scissors" and choice == "paper": #  scissors paper
        print("computer : " , computer)
        print("COMPUTER    WINS !!!!!!!!!!!!!!!!!")
    if  computer == "paper" and choice == "rock": # paper rock
        print("computer : " , computer)
        print("COMPUTER    WINS !!!!!!!!!!!!!!!!!")
    if  computer == "paper" and choice == "scissors": #  paper scissors
        print("computer : " , computer)
        print("YOU   WIN !!!!!!!!!!!!!!!!!")
    if  computer == "scissors" and choice == "rock": # scissors rock
        print("computer : " , computer)
        print("YOU  WIN !!!!!!!!!!!!!!!!!")
    choice = input("Enter your choice :  ")

    
