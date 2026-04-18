import math

def check_positive(*values):
    for value in values:
        if value <= 0:
            raise ValueError("values must be positive")


def circle_area(radius):
    check_positive(radius)
    return math.pi * (radius ** 2)

def circle_perimeter(radius):
    check_positive(radius)
    return 2 * math.pi * radius

def rectangle_area(a, b):
    check_positive(a,b)
    return a * b

def rectangle_perimeter(a, b):
    check_positive(a, b)
    return 2 * (a + b)

def triangle_area(base, height):
    check_positive(base, height)
    return 0.5 * base * height
