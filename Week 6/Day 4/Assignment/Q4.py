''' Write a function called count_vowels(s) that takes a string s
as a parameter and returns the total number of vowels (a, e, i, o, u)
in the string. '''

def count_vowels(s):
    v = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in v:
            count+=1
    print("No of vowels:", count)

count_vowels(s="aeroplane")
