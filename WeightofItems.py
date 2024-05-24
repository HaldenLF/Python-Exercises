def WeightOf():
    numOfWidgets = int(input("How many widgets do you have?: \n"
                             "> "))
    numOfGizmos = int(input("How many gizmos do you have?: \n"
                             "> "))
    
    widgets = 75
    gizmos = 112
    total = numOfWidgets * widgets + numOfGizmos * gizmos
    print("The total order of items is ", total, " grams")

WeightOf()