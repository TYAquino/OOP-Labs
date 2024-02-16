'''
file: Circle-Class.py
Author: Trisha Aquino
Description: A lab classes and objects assignment in Object-Oriented course
Version: Dec. 3, 2023
'''

import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round(math.pi * self.__radius ** 2, 2)
    
    def perimeter(self):
        return round(2 * math.pi * self.__radius, 2)

# Ask user to input the radius
radius = float(input('Enter radius: '))
new_circle = Circle(radius)

# Display the results
print(f"The area of the circle is {new_circle.area()}")
print(f"The perimeter of the circle is {new_circle.perimeter()}")