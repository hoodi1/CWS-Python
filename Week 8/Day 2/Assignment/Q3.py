'''Write a Python class named Rectangle with a constructor that
takes no arguments and prompts the user for the length and width
of the rectangle. The constructor should initialize two instance
variables with the same names. Write a method named area that
calculates and returns the area of the rectangle.'''

class Rectangle:
    def __init__(self) -> None:
        self.length = int(input("Enter length of rectangle : "))
        self.width = int(input("Enter width of rectangle : "))

    def area(self):
        self.a = self.length*self.width
        print(f"Area of rectangel is {self.a}")

re1 = Rectangle()
re1.area()        
