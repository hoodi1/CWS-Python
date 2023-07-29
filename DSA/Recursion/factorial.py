def factorial(n):
    if type(n) != int or n<1:
        return "wrong input"
    else:    
        if n==1:
            return 1
        else:
            return n* factorial(n-1)
    

x = factorial(5)
print(x)