'''Make your own list. Write a Python program that takes an
integer as an input, and make a new list containing the last n
elements of the original list but in reverse order. Using slicing logic.'''

a=[10, -5, 8, 3, -1, -9, 7, 2]

n = int(input("Enter n = "))

b = a[len(a)-n:]

b.reverse()

print(b)