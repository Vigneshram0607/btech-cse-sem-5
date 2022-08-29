"""
SQUARE, RECTANGLE, CIRCLE
"""

import area as a
import volume as v
while True:
    print("Welcome, \n1.SQUARE\n2.RECTANGLE\n3.CIRCLE")
    choice = int(input("Enter Number to Calculate AREA and VOLUME of Specific shape: "))
    if choice == 1:
        side = int(input("Enter side of SQUARE: "))
        a.square_area(side)
        v.square_volume(side)
    elif choice == 2:
        length = int(input("Enter length of RECTANGLE: "))
        width = int(input("Enter width of RECTANGLE: "))
        height = int(input("Enter Height of RECTANGLE: "))
        a.rectangle_area(length, width)
        v.rectangle_volume(length, width, height)
    elif choice == 3:
        radius = int(input("Enter radius of CIRCLE: "))
        a.circle_area(radius)
        v.circle_volume(radius)
    else:
        print("","INVLAID INPUT","",sep = "*"*10)

    if input("Do you want to continue [y/n]: ").lower() == 'n':
        print("\nBye!")
        break
