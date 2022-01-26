# NAME OF AUTHOR: Lucas Galan
# NAME OF THE PROGRAM:  Q1Agechecker
# DATE OF CREATION: Monday January 24 2022 
# PURPOSE OF PROGRAM: chcks to see if you are able to drink alcohol in 

# functions and loop
def get_age():
    while True:
        Age = input("Enter amount: ")
        try:
            
            #This is the part where it checks your age
            checker = int(Age)
            if checker >= 19 :
               #this is the output. If you are above 19 then you get access granted. If not then it says you are underage
                print("Access Granted! Go drink all day and night")
                break
            else:
                print("Access Denied! you cant drink. Wait a few years then try again")
        except ValueError:
            print("Amount must be a number, try again")
    return checker
get_age()