''' 
Put 5 subject name and marks in dict 
Print the total of all marks divisble by 2 
'''

a = {"physics": 69, "chemistry": 80, "maths": 99, "english": 80, "cs": 89}


total = 0
for v in a.values():
    if v%2==0:
        total+=v
print(total)

