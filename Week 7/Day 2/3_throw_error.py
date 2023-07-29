try:
    name = input("Enter name: ") 
    password = input("Enter password: ")
    if name == "admin" and password == "admin":
        print("You successfully logged in !")
    else:
        raise Exception("Wrong login credentials")

except Exception as x:
    print(x)
    
