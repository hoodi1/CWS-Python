"""Write a Python program to display a union and intersection of
2 sets."""

a = {12, 3, 4, 54, 6547, 567, 5675, 12, 12, 12}
b = {12, 22, 4, 54, 6541, 567, 5672, 121, 122, 12}

print(set(a).union(set(b)))
print(set(a).intersection(set(b)))