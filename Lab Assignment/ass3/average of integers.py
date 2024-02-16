'''
file: Average of integers.py
Author: Trisha Aquino
Description: A lab assignment in Object-Oriented course
Version: Oct. 19, 2023
'''

# Get the integer from the user
N = int(input('Enter your integer: '))
i = 0

# Loop it from 1 to N
if N > 1:
    for num in range(1, N + 1, 1):
        i = i + num
    average = i / N     # ---> calculate the integers
    print('Average of', N, 'is', average)   # ---> print the results
   
else:
    print('Only enter integer greater than 1')