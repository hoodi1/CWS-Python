class Student:

    def greet(self):
        print(f"Your name is {self.name}")
        print(f"Your name is {self.age}")
        print(f"Your name is {self.gender}")
    
    def __init__(self, n, a, g):
    #Constructor called when object is created and is also a method 
        self.name = n
        self.age = a
        self.gender = g


s1 = Student("Chirag", 55, "Male")
s2 = Student("Hoodi", 10, "Male")
print("-------")
s1.greet()
print("-------")
s2.greet()
