class Parent:
    def __init__(self) -> None:
        self.fatherName = input("Enter father name = ")
        self.motherName = input("Enter mother name = ")

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()                             #super -> call methods from parent class
        self.childName = input("Enter child name = ")
   
    def displayAll(self):
        print(f"fatherName = {self.fatherName}")
        print(f"motherName = {self.motherName}")
        print(f"childName = {self.childName}")


o = Child()
o.displayAll()