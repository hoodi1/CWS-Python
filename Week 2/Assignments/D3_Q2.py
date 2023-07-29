#Q2
start=int(input("Enter start number = "))
end=int(input("Enter end number = "))

for i in range(start,end+1):
    if i%5==0 or i%7==0:
        print(i,end=" ")