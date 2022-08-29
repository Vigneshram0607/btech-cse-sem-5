"""
Saved as: volume.py;
We use to find volume for specific arguments!
"""


def square_volume(side):
    # side = int(input("Enter side of SQUARE: "))
    print(f"Volume of SQUARE is {side ** 3}")


def rectangle_volume(length, width, height):
    # length = int(input("Enter length of RECTANGLE: "))
    # width = int(input("Enter width of RECTANGLE: "))
    # height = int(input("Enter Height of RECTANGLE: "))
    print(f"Volume of RECTANGLE is {length*width*height}")


def circle_volume(radius):
    # radius = int(input("Enter radius of CIRCLE: "))
    print(f"Volume of CIRCLE/SPHERE is {round((4/3)*(22 / 7)*(radius ** 2), 2)}")
