'''
Write your own dictionary. Then ask a number from a user.
Create a new dictionary with only those key-value pairs having
value greater than those number.
'''

d = {'a': 5, 'b': 2, 'c': 10, 'd': 1, 'e': 9}
x = {}
n = int(input("Enter a number = "))

for k,v in d.items():
    if v>n :
        x[k] = v
print(x)