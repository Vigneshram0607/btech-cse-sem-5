"""
saved as: area.py;
We use to find area for specific Arguments!
"""


def square_area(side):
    # side = int(input("Enter side of SQUARE: "))
    print(f"Area of SQUARE is {side**2}")


def rectangle_area(length, width):
    # length = int(input("Enter length of RECTANGLE: "))
    # width = int(input("Enter width of RECTANGLE: "))
    print(f"Area of RECTANGLE is {length*width}")


def circle_area(radius):
    # radius = int(input("Enter radius of CIRCLE: "))
    print(f"Area of CIRCLE is {round((22/7)*(radius**2), 2)}")
