#print no of times a number has occured in a list

a = [54, 12, 43, 1, 564, 11, 34, 564, 9, 54]
print(a)

for i in range(0,len(a)):
    if a[i]==54:
        print(i)