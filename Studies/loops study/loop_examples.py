'''
display numbers from 0 to 10
'''
print('Solving using while')
# while is pre-test loop
number = 0   # initialization
while number <= 10:
    #loop body is executed if the condition is true
    print(number)
    number = number + 1   # number += 1
    # failing to properly update or forgetting to update the number variable will lead to infinite loop
else:
    print(number)

print('Solving using for loop - no of iterations are known')
for number in range(0,11):
    print(number)

print('increment by 2')
for number in range(0,11,2):
    print(number)
    
print('start value > end value')
for number in range(10,-1):
    print(number)

print('range with only one value')
for number in range(11):
    print(number)
print('Program ends')