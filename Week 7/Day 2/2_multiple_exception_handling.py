''' multiple error handling '''

try:
    a = [254,32,21,32,43,0]
    print(a[4])
    print(a[0] / a[-1])
    #print(b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except IndexError:
    print("Index not present")

except:
    print("some error occurred")  