'''Use loop to work with string'''
course = 'CPRG216'
# index: 0 to len(course) - 1
print('The first character is',course[0])
print('The last character is',course[len(course)-1])
print('The second character from the back is',course[-2])

#use loop to access string characters
print('for loop')
for letter in course:
    print(letter,end=' ')

print('\nfor loop with index')
for i in range(0,len(course)):
    print(course[i],end=' ')
'''Use loop to work with tuple'''
courses = ('CPRG216','CPRG213')
print(type(courses))
print(courses)
print(len(courses))

for c in courses:
    print(c)
    
for i in range(0,len(courses)):
    print(courses[i])
    
'''Use loop to work with list'''
sports = ['Football','Hockey','Volleyball']
print(sports)
print(type(sports))
print(sports[0])

for sport in sports:
    print(sport)

for i in range(0,len(sports)):
    print(sports[i])

