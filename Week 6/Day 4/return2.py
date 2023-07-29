'''
SumList, check

Sumlist(a) -> return sum check odd even
'''

def Sumlist(n : list):
    return sum(n)

def check(x):
    if x%2 == 0:
        print("Even")
    else:
        print("odd")

f = Sumlist([12,23,33,11,23]) 
print(f)
check(f) 
