a = [45, 3, 65, 45, 123, 65, 45, 321, 4, 654]

num = int(input("Enter a number = "))

#if a.count(num) >= 1:
#    print("Yes")
#else:
#    print("No")

if num in a:
    print("Yes")
else:
    print("No")

if num not in a:
    print("Number does not exists")
else:
    print("it exists")