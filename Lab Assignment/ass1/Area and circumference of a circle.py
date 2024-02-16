'''
File: Area and Circumference of a circle.py
Author: Trisha Aquino
Description: A lab assignment in Object-Oriented course
Version: Sep 23, 2023
'''

print('Enter the area and circumference of a circle')

# Area of the circle
# Step 1: input the radius of the area
area = int(input('Enter the radius of the area: '))

# Step 2: calculate the area
pi = 3.14159
radius = pi * area ** 2

# Step 3: display the result
print(f'The answer is: {radius}')


# Circumference of the circle
# Step 1: input the radius of the circumference
cir = int(input('Enter the radius of the circumference: '))

# Step 2: calculate the circumference
radius = 2 * pi * cir

# Step 3: display results
print(f'The answer is: {radius}')

