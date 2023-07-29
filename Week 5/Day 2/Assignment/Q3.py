''' Write a python program to remove all the duplicates from the
string entered by user. '''

a = input("Enter sentence = ")
b = input("Enter a letter = ")
c = []

count = 0
for i in a:
    if i not in c:
        c.append(i)
for i in c:
    print(i,end="")