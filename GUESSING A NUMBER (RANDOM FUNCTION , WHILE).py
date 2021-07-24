# guessing the number
# random -----> is a built in library
# randint ------> function of the library "random"

import random

print("IF YOU WANT TO EXIT IN BETWEEN THE GAME THEN ENTER 0 ")

lower_range = 1
upper_range = 20
user_guess = 0
code_guess = random.randint(lower_range , upper_range)

while (user_guess != code_guess):

     user_guess = int(input("GUESS_A_NUMBER{1 - 20} : "))
     
     if (user_guess > upper_range):
          print("PLEASE PROVIDE THE NUMBER WITHIN THE RANGE")
          continue 

     if (user_guess <= 0):
               print("HAVE A GREAT DAY AHEAD ")
               break

     else:
          if (user_guess > code_guess):
               print("Hint : the number which you guessed is a bit higher than the computer guessed number.")
               print("PLEASE TRY AGAIN : - )")
          elif (user_guess < code_guess):
               print("Hint : the number which you guessed is a bit lower than the computer guessed number.")
               print("PLEASE TRY AGAIN : - )")
else:
     print("WOAH !!!!!  \n YOU MADE IT \n CONGRATULATIONS !!!!!!!!")
          
