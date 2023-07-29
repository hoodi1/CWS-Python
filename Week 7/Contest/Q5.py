'''Write a Python program that takes a user's input for a file
name and a positive integer (n). The program should read the
content of the file and print the nth line. If the file has fewer lines
than the input integer, print a message indicating this. Use
exception handling to deal with non-existent files and invalid
inputs.'''


try:
    m = input("Enter file name: ")
    f = open(m, "r")
    n = int(input("Enter a number: "))

    x = f.read()

    line = x.split("\n")

    print(line[n-1])   

except FileNotFoundError:
    print("Error: File not found")
except:
    print("Error occured : line out of bound")