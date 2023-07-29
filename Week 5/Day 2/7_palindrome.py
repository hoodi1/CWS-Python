# ask user input print yes if palindrome 

a = input("Enter something = ")

if a == a[::-1]:
    print("Yes")
else:
    print("No") 