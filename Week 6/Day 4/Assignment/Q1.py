''' Write a function called sum_natural_numbers(n) that takes
an integer n as a parameter and returns the sum of natural
numbers from 1 to n. '''

def sum_natural_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    print(sum)

sum_natural_numbers(12)