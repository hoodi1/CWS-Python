'''Write a function called union_of_sets(set_a, set_b) that
takes two sets set_a and set_b as parameters and returns a new
set containing the union of the two input sets.'''

def union_of_sets(set_a, set_b):
    print(set_a.union(set_b))

set_a = {1,2,3}
set_b = {3,4,5}
union_of_sets(set_a,set_b)
    