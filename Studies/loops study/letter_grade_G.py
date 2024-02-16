''' Write a program that:
1- asks the user to enter a grade
2- check whether the grade is valid or not and display appropriate message
3- Display the letter grade according to the following:
grade >= 90 --> A+
grade < 90 and grade >= 85 --> A
grade < 85 and grade >= 75 --> B
grade < 75 and grade >= 65 --> C
grade < 65 and grade >= 50 --> D
grade < 50 --> F
'''

grade = float(input('Please enter a valid grade (0-100): '))

if grade >= 0 and grade <= 100:
    print(f'{grade} is valid')
    # nested if to display the letter grade
    if (grade >= 90):
        print('A+')
    elif grade >= 85:
        print('A')
    elif grade >= 75:
        print('B')
    elif grade >= 65:
        print('C')
    elif grade >= 50:
        print('D')
    else:
        print('F')
else:
    print(f'{grade} is not valid')
    
print('Program ends')