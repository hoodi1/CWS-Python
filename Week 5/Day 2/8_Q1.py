a = input("Enter a string = ")

#print(ord(a)) # for string to ascsii conversion

#print(chr(97)) # ascii to char conversion
sum = 0
for i in a:
    sum = sum + ord(i)
print(sum)