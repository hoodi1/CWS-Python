''' Write a python program to ask a string from user. Then count
the number of vowels and number of consonants in that string.
(Make sure there are no spaces in string when you enter in
terminal). '''

n = input("Enter sentence = ")
v ="aeiouAEIOU"

count=0
for i in n:
    for j in v:
        if i == j:
            count+=1
print(count, " no of vowels")
print(len(n)-count, " no of consonants")