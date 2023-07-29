'''Write a Python program to find the length of the longest word
in a string. '''

a = input("Enter a string = ")
b = a.split()
c = []
for i in b:
    c.append(len(i))
print(f"Length of the longest word: {max(c)}")