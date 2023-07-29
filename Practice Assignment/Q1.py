#Q1

import math

n=int(input("Enter a number = "))

if n>=0:
    sr = int(math.sqrt(n))
    s=sr*sr
if s==n:
    print(f"{n} Perfect Square")
else:
    print(f"{n} is not perfect square")