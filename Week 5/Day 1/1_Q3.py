a = { "sagar": [56,78,98,76,88],
     "akul": [67,87,78,98,89],
     "sanjay": [76,77,78,79,75]}

#for every student    sagar -> max marks

for k,v in a.items():
    #print(f"{k} -> {max(v)}")
    max = 0
    for i in v:
        if max < i:
            max = i
    print(f"{k} -> {max}")

