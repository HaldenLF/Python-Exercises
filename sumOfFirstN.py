# This function takes a number from the user and returns 
# the sum of all numbers from 1 to n

def sumOfNum():
    N = int(input("Please enter a positive number: \n"
                  "> ")) # input from user in int form
    
    # if statement to check for positive numbers and 
    # recursively call function until a positive number is entered.
    if N <= 0:
        print("Please enter a positive number\n"
              "---------------------------------\n")
        sumOfNum()
        return

    sum = 0
    # for loop to go add all numbers from 1 to N
    for i in range(1, N + 1):
        sum+=i
    print("The sum of all numbers from 1 to", N, "is", sum)

sumOfNum()