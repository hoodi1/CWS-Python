''' Write a Python program that takes a user&#39;s input for a file name
and reads the content of the file. The program should print the
total number of lines, words, and characters in the file. '''

m = input("Enter file name: ")
f = open(m, "r")

x = f.read()

line = x.split('\n')
print(line)
words = x.split()
charachters = len(x)
print(f"Lines:{len(line)}, Words:{len(words)}, Charachters: {charachters}")

#for i in b:
    
