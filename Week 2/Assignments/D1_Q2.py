#Q2

start=int(input("Enter a start number = "))
end=int(input("Enter a end number = "))

while start<=end:
    if start%5==0 or start%7==0:
        print(start,end=" ")
    start=start+1

    