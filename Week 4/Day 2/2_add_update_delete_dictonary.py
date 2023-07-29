

a = {"physics": 66,"maths": 22}

print(a)

# add
a["history"] = 100       
a[5] = 6
a[10] = 6
print(a)

# update
a["maths"] = 99 
a[10] = 100        
print(a)

#delete
del a["physics"]
print(a)

del a # this will delete the variable "a" 

