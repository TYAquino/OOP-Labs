'''
file: Simple Calculator.py
Author: Trisha Aquino
Description: A lab assignment in Object-Oriented course
Version: Oct. 6, 2023
'''

# Step 1 - ask the user for the operation
print('Choose operation: \nAdd, Subtract, Multiply or Divide')
choice = input('Choice: ').lower()

# Step 2 - process the math
num1 = float(input())
num2 = float(input())

if choice == 'add':
    print(num1, '+', num2, '=', (num1 + num2))
    
elif choice == 'subtract':
    print(num1, '-', num2, '=', (num1 - num2))
        
elif choice == 'multiply':
    print(num1, '*', num2, '=', (num1 * num2))

elif choice == 'divide':
    if num2 == 0:
        print('cannot be divided by zero')
    else:
        print(num1, '/', num2, '=', (num1 / num2))
    
else:
        print('Invalid input')