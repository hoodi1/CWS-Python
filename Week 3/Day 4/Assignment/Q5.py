'''Write a python program to interchange first and last elements
in a list.'''

a=[10, -5, 8, 3, -1, -9, 7, 2]

temp=a[0]
a[0]=a[-1]
a[-1]=temp

print(a)