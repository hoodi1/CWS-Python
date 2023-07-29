a = { "sagar": [56,78,98,76,88],
     "akul": [67,87,78,98,89],
     "sanjay": [76,77,78,79,75]}

'''
name 
marks
1
23
323
321
12
'''

for k,v in a.items():
    print(k)
    for i in v[::-1]:
        print(i)