# NAME OF AUTHOR:  Lucas Galan
# NAME OF THE PROGRAM: NumberGuessingGame
# DATE OF CREATION:  January 25th, 2022
# PURPOSE OF PROGRAM:  play a guessing game with whoever is playing

# VARIABLE DEFINITION
import random
#random module
LowRange = input("Please enter the smallest number in the range of numbers you would like to guess from: ")
# This is setting the lowest number the computer can generate.

HighRange = input("Please enter the largest number in the range of numbers you would like  to guess from: ")
#users says you can only chose a number this high

CorrectNumb = random.randint(int(LowRange),int(HighRange))
#Generates the the number for the user to guess!

attempts = (1)
#trackes amount of attempts
#The attempts start at one


# INPUT
print("It is now time to guess! \n Please enter the number you think is the same one as the computer       generated")
UserAnswer = int(input())
#This is the part where he kills you

# PROCESSING


while UserAnswer != CorrectNumb:
 print("Please try again")
 UserAnswer = int(input())
 attempts = attempts + 1
#The user is promted to attempt at guessing the number again
#The attempts will increase to keep track of attempts
if UserAnswer == CorrectNumb:
  print ("Correct!")
  print("You took",attempts,"to guess correctly")
#Prints the counter(attempts) in a user freindly matter


# OUTPUT
print("thank you for playing the number guessing game! To play again, run the prgram again. May I suggest a larger range?")
#A closing statement to thank the user for playing