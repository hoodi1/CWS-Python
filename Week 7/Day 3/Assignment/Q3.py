"""Ask a word from user. Count the frequency of how many times
that number comes in a file."""

f = open("q1text.txt", "r")

x = f.readlines()

n = input("Enter a word : ")

b = []
for i in x:
    k = i.strip()
    b.append(k)

a = b.count(n)
print(a)