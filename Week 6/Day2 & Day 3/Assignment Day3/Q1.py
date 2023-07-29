'''Write a Python function to find the Maximum and minimum of
three numbers. Use 3 parameters.'''

def maxFun(a, b, c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)

maxFun(12,2,23)