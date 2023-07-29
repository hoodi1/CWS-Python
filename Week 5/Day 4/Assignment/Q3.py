''' Write a Python program to find the most common character in
a string. (Print the letter which repeats most of the time) '''

a = input("Enter a string = ")
b = []
c = []

for i in a:
    b.append(a.count(i))
for i in a:    
    if max(b)== a.count(i):
        if i not in c:
            c.append(i)
print(f"Most common character: {c[0]} ")
      