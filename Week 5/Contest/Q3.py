''' Ask a string from user. Print the characters in a list whose
count is an ODD number. '''

a = input("Enter a string = ")
b = []


for i in a:
    if a.count(i)%2!=0:
        
        if i not in b:
            b.append(i)
print(b)
