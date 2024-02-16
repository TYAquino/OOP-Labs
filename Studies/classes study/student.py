'''
Create a class for students
1- Attributes?
    first_name, last_name, std_id, email, etc.
2- Methods/Functions?
    study()
    getters/setters
'''
class Student:
    '''DocString: brief description of the class'''
    # Class attribute
    profession = 'Student'
    #constructor is called when creating an object
    def __init__(self, fname, lname):
        # instance or non-static attributes
        self.first_name = fname
        self.last_name = lname
        self.email = f'{self.first_name}.{self.last_name}@edu.sait.ca'
    
    # getters
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    # setters
    def set_first_name(self, new_fname):
        self.first_name = new_fname
    
    def set_last_name(self, new_lname):
        self.last_name = new_lname
        
    def set_email(self, new_email):
        self.email = new_email
    #static method
    @staticmethod
    def get_profession():
        return Student.profession
    
    def __str__(self):
        return f'First Name = {self.first_name}\nEmail = {self.email}'  
    def greet(self):
        return 'Hi from student class'

print(Student.__doc__)
print(Student.greet)

#instantiate an object
john = Student('John','Smith')
print(john.greet())
print(john.first_name)
maria = Student('Maria','Dave')
print(maria.first_name)
print(john.email)

print(Student.profession)
print(john.profession)
print(maria.profession)
print(john.get_email())

print(maria.get_email())
print(maria.set_first_name('Kitty'))
print(maria.get_first_name())
print(Student.get_profession())

print(john.__str__())
print(john)
print(str(john))