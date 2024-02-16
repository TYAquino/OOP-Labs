'''Write a program that 
1- keep asking the user to enter a number and stop if the user enters zero\
2- calculate the total and average of the entered numbers
'''
total = 0
counter = 0
number = float(input('Please enter a number and zero to stop: '))
while number != 0:
    total = total + number  #total += number
    counter += 1
    number = float(input('Please enter a number and zero to stop: '))

print(f'total = {total}, average = {total/counter}')