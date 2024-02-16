class Person:
    def __init__(self, person_name, person_age):
        self.__name = person_name
        self.__age = person_age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_name(self, person_name):
        self.__name = person_name

    def set_age(self, person_age):
        self.__age = person_age

    def __str__ (self):
          return f"Name is {self.__name}, age is {self.__age}"
    
def main ():
    persons_list = []   # list of Person objects
    p = Person('Dave', 35)
    persons_list.append(p)
    print (p)
    print (p.get_age())
    # change the age
    p.set_age (61)
    print (p)
    
    p = Person('Hamdy', 35)
    persons_list.append(p)
    print('list contents')
    for person_obj in persons_list:
        print(person_obj)
if __name__ == '__main__':
    main()


