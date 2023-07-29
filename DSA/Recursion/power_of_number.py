# calculate power of a number

def power(b,e):
    if e == 0:
        return 1
    if e == 1:
        return b
    else:
        return b*power(b,e-1)
    
x = power(5,4)
print(x)


