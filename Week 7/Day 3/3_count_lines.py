''' 
abc.txt

number of lines
'''

f = open("abc.txt", "r")
x = f.readlines()
print(x)
print(f"Numbers of lines : {len(x)}")
f.close()