def findElement(myList, num):
    for i in range(0, len(myList)):
        if myList[i] == num:
            return i
    return "Not Found"

a = [32, 43, 65, 11, 32, 100]

print(findElement(a, 43))