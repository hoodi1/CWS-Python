''' Write a Python code to check if a given list is sorted in
ascending order.'''

a = [12, 32, 45, 66, 77, 88, 80]
b = a.copy()

b.sort()

if b == a :
    print("YES")
else:
    print("NO")