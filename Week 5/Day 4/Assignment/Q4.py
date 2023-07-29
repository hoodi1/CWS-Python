''' Write a Python program to remove duplicate characters from
a string and return the modified string. '''

a = input("Enter a string = ")
c = []

for i in a:
    if i not in c:
        c.append(i)
c = "".join(i for i in c)
print(f"Modified string : {c}")