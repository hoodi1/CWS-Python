a = "Aeroplane is a big transport"

#print(a[0])
#print(a[9])
#print(a[-2])
#print(a[2:5])
#print(a[::-1])

#a[0] = "z"  # wont run cause its immutable
#a = "z"     # it will assign a new value z

#for i in range(0,len(a)):
#    #print(i)
#    print(a[i], end=" ")

print(list(a))