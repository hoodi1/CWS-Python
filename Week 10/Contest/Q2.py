'''Write a function to find the intersection of two arrays without
using sets.'''

a = list(map(int,input("Enter list : ").split()))
b = list(map(int,input("Enter list : ").split()))
c = []

for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)      