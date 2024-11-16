import math

def pythagoras(a, b):
    """Calculate the hypotenuse of a right triangle."""
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    """Calculate the area of a circle given its radius."""
    area = math.pi * r**2
    return area
