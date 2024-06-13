import math

latitudeA = math.radians(int(input("What is the latitude of the first point: \n"
                  "> ")))
longtitudeA = math.radians(int(input("What is the longtitude of the first point: \n"
                  "> ")))

latitudeB = math.radians(int(input("What is the latitude of the second point: \n"
                  "> ")))
longtitudeB = math.radians(int(input("What is the longtitude of the second point: \n"
                  "> ")))

distance = 6371.01 * math.acos(
      math.sin(latitudeA) * math.sin(latitudeB) +
      math.cos(latitudeA) * math.cos(latitudeB) * math.cos(longtitudeA - longtitudeB)
  )

print(f"The distance between the two points is: {distance: .2f} kilometers.")