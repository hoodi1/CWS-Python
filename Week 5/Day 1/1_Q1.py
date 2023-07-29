a = { "sagar": [56,78,98,76,88],
     "akul": [67,87,78,98,89],
     "sanjay": [76,77,78,79,75]}

# Print student name along with total marks

for k,v in a.items():
    print(f"{k} has scored {sum(v)}")