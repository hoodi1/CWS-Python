'''Write a Python program that takes a user's input for a file
name and a positive integer (n). The program should read the
content of the file and print the first n lines.'''

m = input("Enter file name: ")

f = open(m, "r")

n = int(input("Enter a +ve int: "))

x = f.readlines()
for i in x[:n]:
    print(i)

