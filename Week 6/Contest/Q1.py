'''Q1. Write a function called list_average(lst) that takes a list of
numbers lst as a parameter and returns the average of the
numbers in the list.'''

def list_average(lst):
    avg = sum(lst)/len(lst)
    print(avg)

lst=[10,20,30,40,50,60]
list_average(lst)