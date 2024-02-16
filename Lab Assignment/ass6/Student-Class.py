'''
file: Student-Class.py
Author: Trisha Aquino
Description: A lab classes and objects assignment in Object-Oriented course
Version: Dec. 3, 2023
'''

class Student:
    profession = 'Student'
    def __init__(self, name, address, id_number):
        self.__student_name = name
        self.__student_address = address
        self.__student_id = id_number
    
    def details(self):
        return f'Name: {self.__student_name} \nID: {self.__student_id} \nAddress: {self.__student_address}'

# Ask the student's inputs for details
Student_name = input('Enter your name: ')
student_id = int(input('Enter your ID number: '))
student_address = input('Enter your address: ')

# Create a new student as an object
student_info = Student(Student_name, student_address, student_id)

# Print student's information
print(student_info.details())