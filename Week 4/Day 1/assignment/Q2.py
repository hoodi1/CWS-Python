'''Write a Python program to find repeated items in a tuple.'''

a = (12, 23, 12, 2, 334, 5, 55, 1, 23,33,33)

a = list(a)

b = []

for i in range(0,len(a)):
    for j in range(0,i):
        if a[i]==a[j]:
            print(a[i])




