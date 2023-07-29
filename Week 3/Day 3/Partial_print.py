""" 
enter start index =
enter end index =
"""

a = [55555, 3, 65, 45, 432, 5436, 756, 86789, 798, 798, 908, 123, 65, 45, 321, 4, 654]

n = int(input("Enter start index = "))
m = int(input("Enter end index = "))

for i in range(n,m+1):
    print(a[i])