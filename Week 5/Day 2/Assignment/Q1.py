''' Write a Python program to check if a string has at least one
letter and one number. If it has at least one letter and one number
then print YES else print NO.'''

a = input("Enter something = ")

isNumber = False
isLetter = False
for i in a:
    if i.isdigit():
        isNumber = True
    elif i.isalpha():
        isLetter = True
if  isNumber == True and isLetter == True:
    print("Both letter and number present")
else:
    print("Not present")
