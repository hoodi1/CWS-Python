#Calculate time complexity

def findMax(a):
    max = a[0]              # o(1)
    for i in a:             # o(n)
        if i > max:         # o(1)
            max = i         # o(1)
    return max              # o(1)

x = findMax([12,23,34,44,45])
print(x)

# TC -> o(n) 
