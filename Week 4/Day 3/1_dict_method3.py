a = {"name": "Chirag", "age": 22, "gender": "Male"}

#a["name"] = "Pankaj"
#a.update({"name": "Pankaj", "physics": 555})

#del a["name"]

# Ask key from user if key exists then delete

keyName = input("Enter key you want to delete = ")
#if a.get(keyName) != None:
if keyName in a:
    a.pop(keyName)
    print(a)
