"""Write a Python program that takes a user's input for a file
name and a word. The program should read the content of the file
and find the line number where the given word first appears. If the
word is not found in the file, print a message indicating this. Use
exception handling to deal with non-existent files."""

try:
    m = input("Enter file name: ")
    f = open(m, "r")
    n = input("Enter a word: ")

    x = f.read()

    line = x.split("\n")

    for i in range(len(line)):
        if n in line[i]:
            print(f"The word {n} appears on line {i+1}")   
        else:
            raise Exception("Word not found!")
    f.close()
except FileNotFoundError:
    print("Error: File not found")
except Exception as x:
    print(x)
except:
    print("Word Not found")

    