''' Write a python program to convert Snake case to Pascal case.
Ask string from user. '''

a = "aeroplane_is_a_good_transport"

a = a.replace('_', ' ')
a = a.title()
a = a.replace(' ', '')
print(a)
