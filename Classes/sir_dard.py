class Abc:
    def setChild(self, childObj):
        self.child = childObj

    def display(self):
        self.child.displayChild()

class Xyz:
    def displayChild(self):
        print("I am a displayChild")

obj= Xyz()
obj1 = Abc()
obj1.setChild(obj)
obj1.display()