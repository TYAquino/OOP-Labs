'''
file: simple-calculator.py
Author: Trisha Aquino
Description: A lab functions assignment in Object-Oriented course
Version: Nov. 10, 2023
'''

def add (num1,num2):     # ---> function for adding two numbers
    return num1 + num2

def subtract (num1,num2):     # ---> function for subtracting two numbers
    return num1 - num2

def multiply (num1,num2):     # ---> function for multiplying two numbers
    return num1 * num2

def divide (num1,num2):     # ---> function for dividing two numbers
    return num1 / num2

print('Choose operation: \nAdd \nSubtract \nMultiply \nDivide')
choice = input('Enter choice: ').lower()

# Ask the user for their inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter first number: '))

# Calculate the numbers
if choice == 'add':
    print(num1, '+', num2, '=', add(num1, num2))
    
elif choice == 'subtract':
    print(num1, '-', num2, '=', subtract(num1, num2))

elif choice == 'multiply':
    print(num1, '*', num2, '=', multiply(num1, num2))

elif choice == 'divide':
    if num1 == 0 or num2 == 0:
        print('Cannot be divided')
    else:
        print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('Invalid input')

print('Done!')