def areaOfRoom():
    length = float(input("Enter the length of the room: "))
    width = float(input("Enter the width of the room: "))

    area = length * width

    return ("The area of the room is ",  area ," sqaure meters")

print(areaOfRoom())