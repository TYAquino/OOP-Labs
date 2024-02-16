'''
file: While loop with errors.py
Author: Trisha Aquino
Description: A lab assignment in Object-Oriented course
Version: Oct. 19, 2023
'''

# the program should be performing a task of adding all intergers I = 1,2,...10
some_number = 0
i = 1
while i < 11:  # ---> it didn't have any colon so I added one for the indented block to be executed
    some_number += i   # ---> I changed the code here to add all the integers that are less than 11
    i += 1	# ---> changing it because if I did the some_number += 1 it'll continue to print infinitely
print(some_number)	# ---> the print statement was missing parenthesis in order for it to work/execute