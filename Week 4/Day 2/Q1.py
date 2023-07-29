a = {}

name = input("Enter name = ")
a['name'] = name

age = int(input("Enter age = "))
a['age'] = age

gender = input("Enter gender = ")
a['gender'] = gender

for i in range(0,5):
    sub = input("Enter subject = ")
    marks = int(input("Enter marks = "))
    a[sub] = marks

print(a)

