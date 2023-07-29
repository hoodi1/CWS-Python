'''Write a Python class named Car with two instance variables
make and model. Write a method named getMakeModel that
returns the make and model of the car as a string.'''

class Car:
    make = ""
    model = ""

    def input(self):
        self.make = input("Enter make of car: ")
        self.model = input("Enter model of car: ")
        
    def getMakeModel(self):
        s = ""
        s = s + self.make+ " " +self.model
        #print(f"The make of car is {self.make} and model of car is {self.model}")
        print(s)

car1 = Car()
car1.input()
car1.getMakeModel()
