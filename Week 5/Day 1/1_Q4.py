a = { "sagar": [56,78,98,76,99],
     "akul": [67,87,78,99,89],
     "sanjay": [76,77,78,79,75]}

# print max marks in dictionary = 98

b =[]

for v in a.values():
    b.append(max(v))

print(max(b))

# print max marks name 

max_marks = max(b)

for k,v in a.items():
    if max_marks in v:
        print(f'{k} -> {max_marks}')    