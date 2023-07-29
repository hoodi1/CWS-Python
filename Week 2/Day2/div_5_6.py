""" enter start 
enter end
print number divisible by 5 and 6"""

i=int(input("Enter start = "))
j=int(input("enter end = "))

while i>=j:
    i=i-1
    if i%5==0 and i%6==0:
        print(i,end=" ")