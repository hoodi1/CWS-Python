''' Write a Python program that takes a user's input for a file
name and tries to read the content of the file. If the file does not
exist, print an error message using exception handling. '''

try:
    m = input("Enter file name: ")
    f = open(m, "r")

    x = f.read()
    print(x)

except FileNotFoundError:
    print("Error: File not found")
