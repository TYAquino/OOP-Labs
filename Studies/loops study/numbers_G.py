'''Implement lab 1 flowchart'''
number = float(input("Please enter a number to check: "))

# implement the diamond to determine is the number >= 0  or not
if (number > 0):
    # if body/block --> executed if the condition is True
    print(f'{number} > 0')
elif number < 0:
    # else if body/block --> executed if the condition is False
    print(f'{number} < 0')
else:
    print(f'{number} = 0')
    
print('Done')