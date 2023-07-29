'''Write a Python function to multiply all the numbers in a list.'''

def ListMultiFun(a: list):
    m = 1 
    for i in a:
        m = m*i
    print(m)

ListMultiFun(a=[1,2,3,4,5])