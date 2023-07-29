class Parent():
    def setParentInfo(self):
        self.fatherName = input("Enter father name = ")

    def displaParent(self):
        print("Display parent")
        print(self.fatherName)

class Child(Parent):
    def setChildInfo(self):
        self.setParentInfo()
        self.ChildName = input("Enter child name = ")

    def displayChild(self):
        print("display child")
        print(self.ChildName)

    def AllInfo(self):
        print(f"Father name -> {self.fatherName}")
        print(f"Child name -> {self.ChildName}")

o=Child()
o.setChildInfo()
o.AllInfo()
        