'''Write a Python function to create and print a list where the
values are square of numbers between 1 and 30 (both included).'''

def SqrList():
    a = []
    for i in range(1,31):
        i = i*i
        a.append(i)
    
    print(a)

SqrList()