# function to check the compounf interest over three years at 4%
def compoundInterest():
    deposit = float(input("How much do you wish to deposit?: \n"
                          "> "))
    interestRate = 0.04 #interest rate at 4%. Change to match

    for year in range(1,4): # year range from 1 to 3. Change to match
        amount = deposit * (1 + interestRate) ** year # total in account per year
        print("Saving after ", year," years: $%.2f" % amount)

compoundInterest()