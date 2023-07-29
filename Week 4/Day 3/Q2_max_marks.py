'''
Find the maximum marks in a dictionary
then print key name of max marks
'''

a = {"physics": 69, "chemistry": 80, "maths": 99, "english": 80, "cs": 89}

#print(max(a.values()))

max_marks = 0
max_marks_sub = ""
for s,m in a.items():
    #print(f"The maximum marks is {m} of {s}")
    if m > max_marks:
        max_marks = m
        max_marks_sub = s

print(max_marks)
print(max_marks_sub)

#b = []
#for m in a.values():
#    b.append(m)
#print(max(b))
