""" Exception Handling """

try:
    a = int(input()) 
    b = int(input())
    print(a / b)

except:
    print("some error occurred")   

else:
    print("else statement") 

finally:
    print("Final statement")
