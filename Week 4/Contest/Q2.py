'''
Write your own dictionary. Write a python code to sort the
dictionary by values.
'''

a = {'a': 5, 'b': 2, 'c': 10, 'd': 1}
b = {}
c = sorted(list(a.values()))

for i in c:
    for k,v in a.items():
        if v == i:
            b.update({k:v})
print(b)

#for k in d.keys():
#    e.append(k)
#for v in d.values():
#    b.append(v)
#b.sort()
#
#for v in b:
#    c.update({e:v})
#
#print(c)



