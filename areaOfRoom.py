def areaOfRoom():
    print("Please enter the width of the room")
    widthInput = input("> ")
    print("Please enter the length of the room")
    lengthInput = input("> ")

    Width = int(widthInput)
    Length = int(lengthInput)

    return Length* Width

print(areaOfRoom())