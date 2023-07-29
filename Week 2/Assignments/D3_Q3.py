#Q3
start=int(input("Enter start number = "))
end=int(input("Enter end number = "))

sum=0
for i in range(start,end+1):
    if i%4==0:
        sum=sum+i
print(sum)