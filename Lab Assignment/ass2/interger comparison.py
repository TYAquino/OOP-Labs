'''
file: Interger Comparison.py
Author: Trisha Aquino
Description: A lab assignment in Object-Oriented course
Version: Oct. 6, 2023
'''

print('Enter two integers:')

# Step 1 - input the integers
num1 = int(input())
num2 = int(input())

# Step 2 - determine whether if it's ><= to each other
if num1 > num2:
    print(num1, 'is larger')

elif num1 < num2:
    print(num2, 'is larger')

else: 
    print('These numbers are equal')

# Step 3 - print 'done'
print('Done!')