a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]
even = []
odd = []

for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(a)
print(even)
print(odd)