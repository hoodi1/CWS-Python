''' Write a python program to split a string on vowels. Ask string
from user. '''

a = "aeroplane is a better transport"
v = ["a", 'e', 'i', 'o', 'u']
b = []
words = ""

for i in a:
    if i.lower() in v:
        if words:                       # checks if not empty
            b.append(words)
            words = ""
    else:
        words = words + i

if words:
    b.append(words)

print(b)
            


        
