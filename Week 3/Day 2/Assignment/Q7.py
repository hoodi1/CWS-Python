# Write a program to find the average of all the numbers present in the list.


a = [65, 23, 44, 12, 2, 766, 123]

sum=0
for i in range(len(a)):
    sum=sum+a[i]

avg=sum/len(a)

print(avg)