'''
file: function-for-circumfernce-and-area-of-a-circle.py
Author: Trisha Aquino
Description: A lab functions assignment in Object-Oriented course
Version: Nov. 10, 2023
'''

import math     # ---> importing math pi equation

# Function to compute the area and circumference of the circle
def area (radius):
    return math.pi * radius ** 2

def circumference (radius):
    return 2 * math.pi * radius

# Input the radius of the area and circumference
radius = float(input('Enter the radius of the circle: '))
print(f'Area of circle is {area(radius):.3f}')
print(f'Circumference of circle is {circumference(radius):.3f}')