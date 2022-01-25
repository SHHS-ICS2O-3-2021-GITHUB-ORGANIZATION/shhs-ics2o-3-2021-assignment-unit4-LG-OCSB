# NAME OF AUTHOR: Lucas Galan
# NAME OF THE PROGRAM: Q2MathDrill
# DATE OF CREATION: January 25th, 2022
# PURPOSE OF PROGRAM: To make a random math equation


# VARIABLE DEFINITION
import random
AddNumb1 = random.randint(1,100)
AddNumb2 = random.randint(1,100)
AddCorrect = AddNumb1 + AddNumb2 

MultiNumb1 = random.randint(1,12)
MultiNumb2 = random.randint(1,12)
MultiCorrect = MultiNumb1 * MultiNumb2

# INPUT
QChoise = int(input("Welcome to multiplication and addition practice to select multiplication please type 1, to select addition type 2, and to leave type 3"))


# PROCESSING
if QChoise == (1):
    print("You have chosen addition! Your question is ")
    print(AddNumb1, "+", AddNumb2)
    AddAnswer = int(input("your answer is :"))
    if AddAnswer != AddCorrect:
        print("Incorrect please try again")#To try again the user will have to stop the program and run again
    if AddAnswer == AddCorrect:
        print("Correct, Great Job!") 

if QChoise == (2):
    print("You have chosen multiplication! Your question is ")
    print(MultiNumb1, "x", MultiNumb2)
    MultiAnswer = int(input("your answer is :"))
    if MultiAnswer != MultiCorrect:
        print("Incorrect please try again")#To try again the user will have to stop the program and run again
    if MultiAnswer == MultiCorrect:
        print("Correct, Great Job!") 


if QChoise == 3:
    print("Goodbye")
# OUTPUT
#the user will finish answering their question the program will finish running, if the user wants to continue they will have to restart the program
print(" if you wish to try again, end program and run again.")