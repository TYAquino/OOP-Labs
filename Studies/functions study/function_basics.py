#greeting the class
#function header
# function without parameters
def greet():
    #doc string
    '''This is a doc string'''
    #function body - Python instructions
    print('Hrllo Class!')

# define another function with parameters
def std_info(std_id, std_name):
    #print(f'ID = {std_id}\nName = {std_name}')
    return f'ID = {std_id}\nName = {std_name}'

def cube(num):
    return num**3

#define a function with optional parameters
def abc(x, y = 12):
    return x*y

#Call the function
greet()
print(type(greet))
print(greet.__doc__)

id = input('Enter a student ID: ')
name = input('Enter a student Name: ')
#positional arguments
#info = std_info(id, name)

#keyword arguments
info = std_info(std_name = name, std_id = id)
print(info)

number = float(input('Please enter a number: '))
print(f'The cube of {number} = {cube(number)}')

print(print(999))
print(abc(3))
print(abc(3,y=10))