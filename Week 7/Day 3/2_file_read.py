'''
3 Types of mode to open a file:
    1. Read (r)
    2. Write (w)
    3. Append (a)
'''

f = open("abc.txt", "r")
#r = f.read()
#print(r)

a = f.readline()
print(a)

b = f.readline()
print(b)

x = f.readlines()
print(x)

f.close()

