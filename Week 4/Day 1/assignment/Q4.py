'''Write a Python program to remove an item from a tuple.'''

a = (1,2,3,4,5,6,7,8,9,12,12,23,3)

a = list(a)

n = int(input("Enter element = "))               
a.remove(n)              # will remove the first left most value if more same values are present                

print(tuple(a))

