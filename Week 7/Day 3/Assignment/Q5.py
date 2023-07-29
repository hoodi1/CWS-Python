'''Write a python program. Only print those lines which contains
‘a’ in it.'''

f = open("q5text.txt", "r")

x = f.read()

y = x.split("\n")
print(y)

for i in range(len(y)):
    if "a" in y[i]:
        print(y[i])