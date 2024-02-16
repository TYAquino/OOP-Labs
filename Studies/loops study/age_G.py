'''Implement lab 1 flowchart 3'''
age = float(input("Please enter a number to check: "))

# implement the diamond to determine whether it is child, teenager, adult
if (age <= 14):
    print('child')
elif (age <= 18):
    print('Teenager')
else:
    print('Adult')
print('Done')