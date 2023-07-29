'''Write a function called find_common_elements(lst1, lst2)
that takes two lists lst1 and lst2 as parameters and returns a list
containing the common elements between the two lists.'''

def find_common_elements(lst1, lst2):
    print(list(set(lst1).intersection(set(lst2))))

find_common_elements(lst1 = [12,23,12,2],lst2 = [12,22,2,3])