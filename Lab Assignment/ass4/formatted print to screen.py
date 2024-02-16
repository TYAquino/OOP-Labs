'''
file: formatted print to screen.py
Author: Trisha Aquino
Description: A lab syntax rules assignment in Object-Oriented course
Version: Oct. 28, 2023
'''

# Define the variables first
pi = 3.14159
x = pi 
y = float(input('Enter your number: '))

# Compute the product z of the variables
z = x * y

# Print the results
print(f'Multiplying {x} and {y} gives{z: .3f}.')