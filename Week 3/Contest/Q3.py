'''Given a Python list, write a program to 
remove all occurrences of item 70.
'''
list1 = [70, 20, 15, 70, 25, 50, 20]

while list1.count(70)>0:
    list1.remove(70)

print(list1)