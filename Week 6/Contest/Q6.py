'''Q6. Write a function called get_factors(n) that takes an integer n
as a parameter and returns a list of its factors, excluding 1 and the
number itself.'''

def get_factors(n):
    a = []
    for i in range(2,n):
        if n%i == 0:
            a.append(i)
    print(a)

n = int(input("Enter a number : "))
get_factors(n)