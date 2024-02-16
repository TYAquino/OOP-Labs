""" Good pratice - Program Header
file: variables.py
description: unit 2 - part 1: Explaining variables, assignment, etc.
Author: Hamdy Ibrahim
Version: Sep 19, 2023
"""
'''Multi-lines comments:
Comments are notes that explain the code
comments are ignored by Python
Not required to comment every line
'''
# Single line comment: added using #

from typing import Final
#Creating a variable
course = "CPRG 216 - OOP1"   #string variable: sequence of characters within '' or ""
print(course)
print(type(course))
print("Course Name is",course)
print("Course Name is "+course)   # + concatenation operator

no_of_students = 20
print(type(no_of_students))
print("No of students =",no_of_students)
print("No of students = "+str(no_of_students))   # + concatenation operator

found = True    # this is boolean variable. It can store True/False
print(type(found))

pi = 3.14159   # float
print(type(pi))

course = 23.5
print(type(course))   # Python dynamically type programming language

course = True
course = 34
course = 'aaaaa'

GST:Final = 0.05
#GST = 0.07

#import constants
import constants as c
print(c.GST)
print(GST)

found = input("Please enter True/False: ")
print(type(found))
found = bool(found)
print(type(found))
print(type(type(found)))

print("The type of found variable is ",type(found))
print("The type of found variable is "+str(type(found)))

print("Welcome in CPRG 216\n\t\t\tHello Class")

# display Hello "Hamdy Ibrahim"
print("Hello \"Hamdy Ibrahim\"")
print('Hello "Hamdy Ibrahim"')

print('Hello \'Hamdy Ibrahim\'')
print("Hello 'Hamdy Ibrahim'")

n1 = 20
n2 = 3
result = n1 * n2
print("Multiplication = ",result)

result = n1 / n2
print("True division = ",result)

result = n1 // n2
print("Floor division = ",result)

result = n1 % n2
print("Remainder = ",result)

result = 5 ** 3
print("5^3 = ",result)

result = 2 + 3 * 5
print(result)

result = (2 + 3) * 5
print(result)

total = 20
total += 1   # total = total + 1
print(total)

total *= 10   # total = total * 10
print(total)

prompt = 'Please enter your name: '
name = input(prompt)
print(type(name))
print('You entered '+name)
print('You entered {}'.format(name))

age = 37
print('Your name is {} and you are {} years old'.format(name,age))
print('Your name is {0} and you are {1} years old'.format(name,age))
print(f'Your name is {name} and you are {age} years old')
print("Your name is "+name+" and you are "+str(age)+ " years old")