#Q3

n=int(input("Enter a number = "))

r=0
for i in range(n+1):
    r=(r*10)+(n%10)
    if n==0:
        break
    else:
        n=n//10     # // is used for integer value
print(int(r/10))
