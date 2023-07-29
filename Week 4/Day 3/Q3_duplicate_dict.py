""" 
change marks to pass or fail
"""

a = {"physics": 32, "chemistry": 80, "maths": 94, "english": 80, "cs": 89}

for s,m in a.items():
    
    if m > 32:
        a[s] = "pass"
    else:
        a[s] = "fail"
    
print(a)


