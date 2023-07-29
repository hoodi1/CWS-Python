# add 5 elements but list prints in reverse

a=[]
n=int(input("Enter number of elements = "))
for _ in range(0,n):
    num = int(input("Enter number = "))
    a.insert(0,num)
print(a)