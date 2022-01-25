# NAME OF AUTHOR: Lucas Galan
# NAME OF THE PROGRAM: Q2Average
# DATE OF CREATION: January 25th, 2022
# PURPOSE OF PROGRAM: calculates average of numbers given by user

# VARIABLE DEFINITION 
addedSum = (0)
Average = (0) 
counter = (0)


# INPUT
nonZeroNumb = float(input("Enter your numbers (when ready type 0 to Exit): ")) #reciving the numbers to calculate

# PROCESSING
while nonZeroNumb != 0:  # the program counts the amount of numbers added
    addedSum = addedSum + nonZeroNumb
    nonZeroNumb = float(input())
    counter = counter + 1

addedSum = addedSum + nonZeroNumb #adds all numbers togeather to get sum 
Average = addedSum/counter #calculates  average


# OUTPUT 
print ("Total sum of entered number is", addedSum) #prints the sum of all numbers entered
print("Total average of entered number is", Average)