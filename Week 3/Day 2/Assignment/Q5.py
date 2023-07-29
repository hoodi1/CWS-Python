''' Write a python program which prints all the values whose
count is greater than 3. (Make sure to make a list with at least 15
numbers) '''


a = [1, 23, 33, 12, 33, 12, 22, 23, 1, 234, 234, 12, 22, 22, 22, 33, 33, 23, 23]
b = []

for i in a:
    if i not in b:
        b.append(i)

for i in b:
    count = a.count(i)
    if count > 3:
        print(i)