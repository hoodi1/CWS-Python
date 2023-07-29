""" ask a no and print factors of that number"""
count=0
sum=0
a=int(input("Enter a number = "))

for i in range(1,a+1):
    if a%i==0:
        count=count+1
        sum=sum+i
print(count)
print(sum)