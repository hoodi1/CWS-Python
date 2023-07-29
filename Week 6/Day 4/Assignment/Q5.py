'''Write a function called is_prime(n) that takes an integer n as
a parameter and returns True if the number is prime, otherwise
False.'''

def is_prime(n):
    prime = True
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print(prime)
    else:
        prime = False
        print(prime)
    
is_prime(13)