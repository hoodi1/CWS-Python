'''Q3. Write a function called filter_even_numbers(lst) that takes a
list of integers lst as a parameter and returns a new list containing
only the even integers from the input list.'''

def filter_even_numbers(lst):
    b = []
    for i in lst:
        if i%2==0:
            b.append(i)
    print(b)

lst = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
filter_even_numbers(lst)