'''Write a Python program to check if a string is an isogram (no
repeating characters).'''

a = input("Enter a string = ")
c = []

for i in a:
    if i not in c:
        c.append(i)
c = "".join(i for i in c)
if a == c:
    print("Yes, the string is an isogram")
else:
    print("No, the string is an isogram")
    