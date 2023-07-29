'''Take an input from user. Check if the number is prime or not. If
number is not prime, raise your own exception. Remember to
handle all other exceptions. '''


try:
    n = int(input("Enter a number : "))
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        print("Prime")
    else:
        raise Exception("It is not prime")      
except Exception as x:
    print(x)    

except:
    print("Some error occured")    
