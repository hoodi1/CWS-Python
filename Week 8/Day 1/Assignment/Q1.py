'''Write a Python class named Rectangle with two variables
length and width. Write a method named area that calculates
and returns the area of the rectangle.'''

class Rectangle:
    length = 0
    width = 0
    def input(self):
        self.length = int(input("Enter length = ")) 
        self.width = int(input("Enter width = "))

    def area(self):
        area = self.width*self.length 
        print(f"Area is {area}")

    def parameter(self):
        para = 2*(self.width + self.length)
        print(f"Parameter is {para}")

a = Rectangle()
a.input()
a.area()
a.parameter()