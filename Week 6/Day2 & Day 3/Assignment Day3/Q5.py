'''Write a Python function that checks whether a passed string is
palindrome or not.'''

def checkPalid(a):
    if a == a[-1::-1]:
        print("String is palindrome")
    else:
        print("Not palindrome")

checkPalid(a = "strts")