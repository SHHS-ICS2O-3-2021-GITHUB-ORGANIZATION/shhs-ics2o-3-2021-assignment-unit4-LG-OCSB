# NAME OF AUTHOR: Lucas Galan
# NAME OF THE PROGRAM: Q2Average
# DATE OF CREATION: January 25th, 2022
# PURPOSE OF PROGRAM: calculates average of numbers given by user

# VARIABLE DEFINITION 
import numpy as np 
 #this asks for input of numbers
num1 = int(input("Enter the Number 1: ")) 
num2 = int(input("Enter the Number 2: ")) 
num3 = int(input("Enter the Number 3: ")) 
#calculating average
average = (np.sum([num1, num2, num3])) / 3 
#output/answer
print(int(average)) 