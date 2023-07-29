# "Remove" multiple times occuring no from list 

a = [74, 85, 21, 23, 21, 23, 85, 44, 21]

while a.count(21)>0:
    a.remove(21)
print(a)

#alternate way   This method creats a new list from the elements of prev list excluding the number u want to remove 
 
b=[]
for i in range(0,len(a)):   
    if a[i]!=23:
        b.append(a[i])
print(b)