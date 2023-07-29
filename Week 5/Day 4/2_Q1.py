a = "aeroplane is a good mode of transport good bye ok done"
#b = a.split()
#print(b)

#for i in range(0,len(b),2):
#    print(b[i],end=" ")

#b = a.split()[::2]
print(" ".join(i for i in a.split()[::2]))


