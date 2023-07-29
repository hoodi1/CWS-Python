#remove even values 

a = [74, 85, 21, 23, 21, 23, 85, 44, 21]
b=[]
c=[]

for i in range(0,len(a)):
    if a[i]%2 != 0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)