import math
def circle_area (radius):
    if radius < 0:
        return valueError('radius cannot be negative')
    return math.pi * radius * radius
def circle_perimeter (radius):
    if radius < 0:
        return ValueError('radius cannot be negative')
    return 2* math.pi* radius
def rectangle_area (width, height):
    if width < 0 or height < 0:
         return ValuError('Width and height cannot be negative')
    return width* height

def rectangle_perimeter(width,height):
    if width <= 0 or height <= 0:
        return ValuError('Width and height cannot be negative')
    return 2* width*height
def triangle_area(base, height):
    if base <= 0 or height <= 0:
        return ValueError('base or height cannot be nagative')
    return 0.5 * base* height
