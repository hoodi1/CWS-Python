'''Ask a number from user. Pass that number as a parameter to
a function. Check if the number is prime or not.'''

def primeOrnot(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count=count+1
    if count==2:
        print("Prime Number")
    else:
        print("composite number")

n = int(input("Enter a number : "))

primeOrnot(n)