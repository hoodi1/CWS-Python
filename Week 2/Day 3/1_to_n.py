""" 
ask a number 
print 1 to n
divisble by 8"""

a=int(input("Enter a number = "))
count=0
sum=0
for i in range(1,a+1):
    if i%8==0:
       count=count+1
       sum=sum+i
       
print(count) 
print(sum) 
