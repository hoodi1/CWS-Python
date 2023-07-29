a = {"name": "Chirag", "age": 22, "gender": "Male"}

print(a)

''' clear'''
#a.clear()
#print(a)

'''copy ''' 
b = a.copy()
print(b)
a["city"] = "Kanpur"
print(a, b)


'''get'''
r = a.get("name")
print(r) 

r = a.get("nameee")    # if its not in dictionary it wont give error just print "None"
print(r)       

'''None'''
#a = None
#print(a, type(a))

#
keyname = input("Enter key name = ")
if a.get(keyname) != None:
    print(a[keyname])
else:
    print("Key does not exist")