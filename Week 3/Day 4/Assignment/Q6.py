'''Write a Python code to split a list into two halves using list
slicing. (Keep the length of list even)'''

a=[10, -5, 8, 3, -1, -9, 7, 2]

n=int(len(a)/2)

b = a[0:n]
c = a[n:]

print(b)
print(c)