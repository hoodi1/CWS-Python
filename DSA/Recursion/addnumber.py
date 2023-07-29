def addNum(n):
    if type(n) != int or n<1:
        return "wrong input"
    else:
        if n == 1:
            return 1
        else:
            return n + addNum(n-1)
    
x = addNum(10)
print(x)