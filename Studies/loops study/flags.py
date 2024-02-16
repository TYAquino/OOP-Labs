'''flag is a boolean variable
    it can be used with if and while'''
'''Write a program which:
- asks the user to enter grades and stop when enters a -ve value
- calculates the average of these grades'''

repeat = True
total = 0
counter = 0
while repeat:   # equal to repeat == True
    grade = float(input('please enter a grade and -ve grade to stop: '))
    if grade < 0:
        repeat = False
    else:
        counter += 1
        total += grade
        
print(f'Total = {total}')
print(f'Average = {total/counter}')