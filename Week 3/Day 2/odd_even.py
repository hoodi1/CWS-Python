a = [2, 5, 6, 9, 11]
count=0
count2=0
for i in range(len(a)):
    if a[i]%2==0:
        count=count+1
    else:
        count2=count2+1
print(f"Even numbers = {count}")
print(f"Odd numbers = {count2}")
