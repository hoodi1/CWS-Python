""" 
Classes and objects
"""

class Student:
    # Data members/attribute which are variables basically
    #name = ""
    #age = 0
    #gender = ""

    # Methods which are functions basically
    def greet(self):
        print("This is a greet method")
        print(f"Your name is {self.name}")
        print(f"Your name is {self.age}")
        print(f"Your name is {self.gender}")

    def getData(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.gender = input("Enter gender: ")
        #self.city = "Kanpur"


s1 = Student()      # Object
s2 = Student()      # Object
s3 = Student()      # Object
s1.getData()
s1.greet()
print("-------")
s2.getData()
s2.greet()
print("-------")
#s3.greet()
#print(s1)
#s1.name = "Chirag"
#s1.age = 22
#s1.gender = "Male"
#s2.name = "Hoodi"
#s2.age = 10
#s2.gender = "Male"
#print(s1.name,s1.age,s1.gender)   
#print(s2.name,s2.age,s2.gender)    
   