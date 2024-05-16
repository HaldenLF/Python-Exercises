def bottleDeposit():

    smallDeposit = 0.10
    largeDeposit = 0.25
    containerAmount = 0
    total = 0

    small = int(input("How many small containers are there?\n"))
    large = int(input("How many large containers are there?\n"))

    containerAmount =  small * smallDeposit
    print("There is $%.2f" % containerAmount, "worth of small containers\n")

    total += containerAmount

    containerAmount = large * largeDeposit
    print("There is $%.2f" % containerAmount, "worth of large containers\n")
    
    total += containerAmount

    print("Total of $%.2f" % total,"worth of returned containers.\n")
    
bottleDeposit()