import datetime
import time


t1 = datetime.datetime.now()
# for i in range(1, 50000001):
#     a.append(i)
a = [i for i in range(1, 50000001)]
t2 = datetime.datetime.now()
print(t2 - t1)