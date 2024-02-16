'''break and continue'''
for number in range(1,5):
    print(number)
    if (number == 3):
        break   # will terminate the loop
    
print('continue will terminate the current iteration')
for number in range(1,5):
    if (number == 3):
        continue   
    print(number)