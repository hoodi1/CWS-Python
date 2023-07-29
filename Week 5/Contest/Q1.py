''' Count number of alphabets in a string entered by user. '''

a = "abcd1234 xyz"

count = 0
for i in a:
    if i.isalpha():
        count += 1
print(count)


#print(a.count(a.isalpha()))