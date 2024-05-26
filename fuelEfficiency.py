# converts from miles per gallon to litres per 100km

def mpgToL100km():
    # conversion factor for mpg to lkm
    conversion = 235.215
    # user input
    mpg = int(input("What is your cars fuel effiicney in MPG?: "))
    # calculation for km per gallon
    kmPerGalllon = 1/(mpg/conversion)
    # calculation for litre per gallon
    lkm = 100 /kmPerGalllon

    print(f"{mpg} MPG is approximately {lkm:.2f} L/100km.")

mpgToL100km()
