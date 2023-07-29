# ask sentence 
#ask letter 
#if exists enter new

n = input("Enter sentence = ")
a = input("Enter letter = ")

if a in n:
    b = input("Enter new letter = ")
    n = n.replace(a, b)
    print(n)
else:
    print("Letter does not exists") 