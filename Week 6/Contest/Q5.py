'''Q5. Write a function called is_palindrome(s) that takes a string s
as a parameter and returns True if the string is a palindrome
(reads the same forward and backward), otherwise False.'''

def is_palindrome(s):
    if s == s[-1::-1]:
        print(True)
    else:
        print(False)
    
s = "racecar"
is_palindrome(s)