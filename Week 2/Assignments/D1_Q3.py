#Q3

sum=0
start=int(input("Enter a start number = "))
end=int(input("Enter a end number = "))

while start<=end:
    if start%4==0:
        sum=sum+start
    start=start+1
print(sum)
