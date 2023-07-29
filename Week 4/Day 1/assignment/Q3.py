'''Write a Python program to check whether an element exists
within a tuple.'''


a = (1,2,3,4,5,6,7,8,9,12,12,23,3)

n = int(input("Enter tuple element = "))

if a.count(n)>0:
    print("Element exists")
else:
    print("Element doesnt exists")
    
    
