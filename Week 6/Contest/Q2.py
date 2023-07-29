'''Q2. Write a function called dictionary_value_sum(d) that takes a
dictionary d as a parameter, where the values are numbers, and
returns the sum of all the values in the dictionary.'''

def dictionary_value_sum(d):
    sum = 0
    for v in d.values():
        sum = sum + v
    print("sum of all values are: ", sum)

d = {"score1":10, "score2":20, "score3": 30}
dictionary_value_sum(d)