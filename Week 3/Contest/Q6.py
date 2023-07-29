'''There is a list which contains both strings and integers. Count the number of strings and integers present in the list.
'''

a = [1, 2, '3', 'abc', 6, 'ccc', 9]

count = 0
count2 = 0
for i in range(0,len(a)):
    if type(a[i]) == int:
        count = count + 1
    elif type(a[i]) == str:
        count2 = count2 +1
print(f'No of integers = {count}')
print(f'No of strings = {count2}')