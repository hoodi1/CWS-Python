def printNumber():
    start = int(input("Enter start number : "))
    end = int(input("Enter end number : "))
    sum = 0
    for i in range(start,end+1):
        sum = sum + i
    print(f"Sum from {start} to {end} is : {sum}")

printNumber()