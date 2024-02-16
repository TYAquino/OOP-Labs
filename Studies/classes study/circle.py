import math
class Circle:
    '''Static members
    1- Created out of any function/method or at the class level
    2- static members can be accessed using class name or object name
    3- They are shared between objects
    '''
    no_of_circles = 0   #static/class
    def __init__(self, radius):
        #Non-static/instance members --> accessed through objects
        #self.radius = radius   # public
        self.__radius = radius   #private
        Circle.no_of_circles += 1

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        self.__radius = new_radius
    
    def get_area(self):
        return math.pi * self.__radius ** 2
    
    @staticmethod
    def get_no_of_circles():
        return Circle.no_of_circles
     
c1 = Circle(10)
print(c1.get_radius())
print(Circle.no_of_circles)
print(c1.no_of_circles)

c2 = Circle(30)
print(c1.no_of_circles)
print(c2.no_of_circles)
Circle.no_of_circles = 20
print(c1.no_of_circles)

print(Circle.get_no_of_circles())