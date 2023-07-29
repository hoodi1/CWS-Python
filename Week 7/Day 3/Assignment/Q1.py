''' Make a text file. Enter random numbers in that file. Each line
must contain only one number. Write a python program to
calculate the sum of all the numbers. '''

f = open("q12text.txt", "r")

x = f.readlines()
print(x)
b = []
for i in x:
    n = int(i.strip())
    b.append(n)
print(b)
print(sum(b))

f.close()
