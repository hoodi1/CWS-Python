a = (12, 321, 34, 432, 54, 11)

print(a, type(a))
b = list(a)
print(b, type(b))
b.append(100)
a = tuple(b)
print(a, type(a))

