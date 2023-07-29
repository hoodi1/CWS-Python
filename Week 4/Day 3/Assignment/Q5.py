'''
Write a Python program to remove duplicates from Dictionary.
Sample dictionary: dictionary = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10,
7:60, 8:50}
'''
a = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7:60, 8:50}

b = {}


for k,v in a.items():
    if v not in b.values():
        b[k] = v
print(b)