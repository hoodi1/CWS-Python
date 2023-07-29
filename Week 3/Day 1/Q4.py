a = [10, 54, 78, 74, 85, 74, 84, 114, 44, 55, 55, 55, 55]

count=0
for i in range(0,len(a)):
    if a[i]==55:
        count=count+1

print(count)