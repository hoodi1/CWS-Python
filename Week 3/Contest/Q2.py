'''Given a two Python list. Write a program to iterate both lists
simultaneously and display items from list1 in original order and 
items from list2 in reverse order. (Both lists should have same length)'''

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in range(0,len(list1)):
    print(list1[i], list2[len(list2)-i-1])

