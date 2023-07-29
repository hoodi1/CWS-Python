''' Write a Python program to find the most frequent word in a
string. '''

a = input("Enter a string : ")
a = a.split()
b = []
c = []

for i in a:
    b.append(a.count(i))
for i in a:    
    if max(b)== a.count(i):
        if i not in c:
            c.append(i)
print(f"Most frequent word is : {c[0]}")
