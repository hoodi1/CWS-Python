a = {"physics": 66,"maths": 22, "chem": 77}

'''keys'''
r = a.keys()
print(r)

for i in a.keys():
    print(i, a[i])
    #print(f"marks in {i} are {a[i]}")

'''values'''
for i in a.values():
    print(i)

total = 0
for v in a.values():
    total += v
print(f"total is = {total}")

'''items'''
for k,v in a.items():
    print(f"marks in {k} are {v}")