''' reverse per word'''

user_string = "aeroplane ok is a good mode of a transport good bye ok done"

b = user_string[::-1].split()
b.reverse()
print(" ".join(i for i in b))

print(" ".join(i[::-1] for i in user_string.split()))       # one liner using list comprehension
