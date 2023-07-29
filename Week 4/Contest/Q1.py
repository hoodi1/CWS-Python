''' 
Make your own dictionary. Write a Python code where the keys
and values are inverted. The values in the original dictionary
should be unique, ensuring that the inverted dictionary is valid.
'''

a = {'a': 300, 'b': 200, 'c': 400} 
b = {}

for k,v in a.items():
    b[v] = k

print(b)
