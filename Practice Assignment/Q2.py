#Q2

n=int(input("Enter a number = "))

sum=0
for i in range(n+1):
    sum=sum+n%10
    n=int(n/10)
print (sum)