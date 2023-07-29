'''Make 2 different list. First merge both list into third variable. And
sort the merge list in descending order.  '''


a = [65, 23, 44, 12, 2, 766, 123]
b = [1, 234, 12, 22, 22, 22, 33, 33, 23, 23]
c = []

c.extend(a)                                 # merging list a in c
c.extend(b)                                 # merging list b in c
print(c)    
c.sort(reverse=True)                        # sorting in descending order
print(c)
