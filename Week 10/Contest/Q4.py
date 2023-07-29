'''Implement a function to find the missing number in a given
range of integers.'''

def findMissingNumber(n):
    for i in range(n[0],n[-1]):
        if i not in n:
            print(i)
    else:
        print(None)

x = list(map(int,input("Enter list : ").split()))
findMissingNumber(x)