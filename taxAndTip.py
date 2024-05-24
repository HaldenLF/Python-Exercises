def taxAndTip():
    # get user to input cost of meal
    costOfMeal = float(input("How much was the meal>: \n"
                             "> "))
    tax = costOfMeal * 0.10 # local tax
    tip = costOfMeal * 0.18 # tip rate
    total = costOfMeal + tax + tip # total cost of meal
    print("The total cost of the meal is $%.2f" % total)

taxAndTip()