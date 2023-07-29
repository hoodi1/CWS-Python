''' Write a function that inputs a number and prints the
multiplication table of that number. '''

def MultiTable():
    n = int(input("Enter a number : "))
    for i in range(1,11):
        i = i*n
        print(i)

MultiTable()