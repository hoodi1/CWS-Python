''' Take 10 integer inputs from user and store them in a list. Now,
copy all the elements in another list but in reverse order. '''

a=[]                    #first list with user input numbers
b=[]                    #2nd list reverse
for i in range(10):
    n=int(input("Enter number = "))         
    a.append(n)         # adding numbers to list a
print(a)
a.reverse()             # reversing list a

for i in range(10):
    b.append(a[i])                  
print(b)