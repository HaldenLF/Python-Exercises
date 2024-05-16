def areaOfField():

    acre = 43560 # square footage of acre

    length = float(input("Enter the length of the field in feet: "))
    width = float(input("Enter the width of the field in feet: "))

    area = length * width / acre  

    print("The area of the field is",  area ,"acres.")

areaOfField()