# n -> enter number print all the factors of n in list

n = int(input())
print("prime" if len([i for i in range(1,n+1) if n%i==0]) == 2 else "consonant")