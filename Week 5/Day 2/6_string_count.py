a = input("Enter sentence = ")
b = input("Enter a letter = ")

count = 0
for i in a:
    if i == b:
        count+=1
if count > 0:
    print("yes")
else:
    print("no")