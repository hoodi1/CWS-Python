#Q4

a=int(input("Enter number one 'a' = "))
b=int(input("Enter number two 'b' = "))
c=int(input("Enter number three 'c' = "))

if a>b and a>c:
    print(f"a is the largest number = {a}")
elif b>c and b>a:
    print(f"b is the largest number = {b}")
else:
    print(f"c is the largest number = {c}")
