# user input dictionary

n = int(input("Enter a number = "))
a = {}

for i in range(0,n):
    sub = input("Enter subject = ")
    marks = int(input("Enter marks = "))
    a[sub] = marks

print(a)