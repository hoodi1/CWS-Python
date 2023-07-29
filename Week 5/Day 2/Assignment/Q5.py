''' Write a python program to only print second half of the string.
Ask string from user.'''

a = input("Enter something = ")

print(a[len(a)//2:])


#b = len(a)/2
#if type(len(a)/2) == int:
#    print(a[(len(a)/2):])
#else:    
#    print(a[int(len(a)/2)+1:])
