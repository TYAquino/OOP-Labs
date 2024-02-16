'''
file: average-of-integers.py
Author: Trisha Aquino
Description: A lab functions assignment in Object-Oriented course
Version: Nov. 10, 2023
'''

# Function to compute the integers from the user's input
def average (N):
    i = 0
    for num in range(1, N + 1, 1):
        i = i + num
    return i / N

# Ask the user for their input
N = int(input('Enter the integer: '))

# It should print 'invalid' if the user inputs < 1
if N > 1:
    total = average(N)
    print(f'The average of', N, 'is:', total)
else:
    print('Only input integer greater than 1')