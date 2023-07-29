''' Given a list of integers, write a program to find the sum of all positive numbers and the product of all negative numbers.'''

a = [1, 2, -3, 4, -5, -6, 7]

sum = 0
pro = 1
for i in range(0,len(a)):
    if a[i] >= 0:
        sum = sum + a[i]
    else:
        pro = pro * a[i]

print(f'Sum of all positive numbers = {sum}')
print(f'Product of all negative numbers = {pro}')

