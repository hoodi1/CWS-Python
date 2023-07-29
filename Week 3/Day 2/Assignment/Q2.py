# Ask 10 numbers from the user and put them into the list. Now remove all the even numbers from that list.


a = []
for i in range(10):
    n = int(input("Enter a number = "))                 # user input for list
    a.append(n)
print(a)

b = []
for i in range(10):
    if a[i]%2!=0:                                       # if odd 
        b.append(a[i])

print(b)                                                # list with only odd numbers
