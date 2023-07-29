'''Write a Python class named Employee with a constructor that
takes a name, an age, a salary, and a department as arguments
and initializes four instance variables, name, age, salary, and
department. Write a method named promote that increases the
salary of the employee by a certain percentage.'''

class Employee:
    name = ""
    age = ""
    salary = 0
    department = ""

    def __init__(self,n,a,s,d):
        self.name = n
        self.age = a
        self.salary = s
        self.department = d

    def promote(self,percentage):
        self.salary_hike = self.salary*(percentage/100)
        self.salary_after_hike = self.salary + self.salary_hike
        print(f"Salary after promotion is ${self.salary_after_hike}")

emp1 = Employee("Vijay",23,40000,"IT")
emp1.promote(50)

        