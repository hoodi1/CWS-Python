try:
    a = int(input("Enter number 1 = "))
    b = int(input("Enter number 2 = "))
    c = int(input("Enter number 3 = "))
    print(a + b + c)

except ValueError:
    print("Enter proper integer valuea")

except:
    print("Some error occurred")