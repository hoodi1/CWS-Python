

for i in range(1,10):
    if i==5:
        break           #breaks the loop if condition true
    print(i,end=" ")


print("  ",end=" ")

for i in range(1,10):
    if i==5:
        continue        #skips the lines below it and continues the loop
    print(i,end=" ")