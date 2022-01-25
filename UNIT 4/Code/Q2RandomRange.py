# NAME OF AUTHOR:Lucas Galan
# NAME OF THE PROGRAM:  Q2RandomRange
# DATE OF CREATION:  January 25th, 2022
# PURPOSE OF PROGRAM:  Generates a number between a set range


# VARIABLE DEFINITION variables and input
#Var1 = input()
#Var2 = input()

# INPUT: range
print ("Give two numbers and random number generator will generate one between the two given")
Var1= int(input())
Var2= int(input())


# PROCESSING
import random
Kelp = random.randint(Var1,Var2)




# OUTPUT
print("The number generateor has produced")
print(Kelp)
print("as your number")