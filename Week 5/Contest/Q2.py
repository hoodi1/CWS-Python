'''Write a python program to capitalize the first and last
character of each word in a string entered by user. '''

a = "hello world"

#a = a.title()
#a = a[0:1].upper() + a[1:len(a)-1] + a[len(a)-1:len(a)].upper()
#b = a[::-1].split()
#b.reverse()

#c = " ".join(i for i in b)
#print(c)

b = a.split()

for i in b:
    if len(i) == 1:
        print(i.upper(), end = " ")
    else:
        print(i[0].upper() + i[1:len(i)-1] + i[-1].upper(), end = " ")








#print(" ".join(i for i in b))


