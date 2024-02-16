'''
File: Area of Trapezoid.py
Author: Trisha Aquino
Description: A lab assignment in Object-Oriented course
Version: Sep 23, 2023
'''

print('Enter the given bases and height of the trapezoid')

# Step 1: get the bases and height of the Trapezoid
base_1 = int(input('a Base: '))
base_2 = int(input('b Base: '))
height = int(input('Height: '))

# Step 2: calculate
area = (base_1 + base_2) * height / 2

# Step 3: display the result
print(f'The answer is: {area}')
