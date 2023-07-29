'''Given a list of numbers. Write a program to turn 
every item of a list into its square '''

numbers = [1, 2, 3, 4, 5, 6, 7]

for i in range(0,len(numbers)):
    numbers[i] = numbers[i]**2
print(numbers)