'''
file: function-for-area-of-a-rectangle.py
Author: Trisha Aquino
Description: A lab functions assignment in Object-Oriented course
Version: Nov. 10, 2023
'''

# Function to compute the area of a rectangle
def rectangle (length, width):
    return length * width

# Input the length and width of the rectangle
length = float(input('Enter length: '))
width = float(input('Enter width: '))
print(f'The area of the rectangle is {rectangle(length, width)}')