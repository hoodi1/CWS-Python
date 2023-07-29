''' Ask a word from user. Print Yes or No if the word entered by
user exists in a file or not. '''

f = open("q1text.txt", "r")

x = f.readlines()

n = input("Enter a word : ")

b = []
for i in x:
    k = i.strip()
    b.append(k)

if n in b:
    print("YES")
else:
    print("NO")

f.close()