'''
file: Multiples.py
Author: Trisha Aquino
Description: A lab assignment in Object-Oriented course
Version: Oct. 6, 2023
'''

print('Enter the integers:')

# Step 1 - ask the user of the integers
num1 = int(input())
num2 = int(input())

# Step 2 - process
if (num1 % num2 == 0):
    print('the number is divisible')
else:
    print('the number is not divisible')