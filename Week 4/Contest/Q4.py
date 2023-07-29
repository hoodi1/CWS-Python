'''
Make 2 dictionary dict1 and dict2. Write a new dictionary
containing the keys that are present in dict1 but not in dict2.
'''

dict1 = {'a': 5, 'b': 2, 'c': 10, 'd': 1, 'e': 9}
dict2 = {'f': 5, 'x': 2, 'c': 10, 'd': 1, 'e': 9}
dict3 = {}

for k,v in dict1.items():
    if k not in dict2:
        dict3[k] = v
print(dict3)