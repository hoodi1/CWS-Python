'''Write a function to find the first non-repeating character in a
string.'''

a = input("Enter a string: ")
for i in a:
    if a.count(i)==1:
        print(i)
        break
else:
    print(None)
