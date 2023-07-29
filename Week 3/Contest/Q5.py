'''Given a list of integers, print all the prime numbers present in the list.
'''

a = [ 11, 3, 2, 7, 37, 44, 55, 40]

for i in a:
    count = 0
    for j in range(1,i):
        if i % j == 0:
            count += 1
    if count == 1:
        print(i,end=" ")