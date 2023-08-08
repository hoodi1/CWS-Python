import math

def bubbleSort(customList):
    for i in range(0,len(customList)-1):
        for j in range(1,len(customList)):
            if customList[j-1] > customList[j]:
                customList[j-1],customList[j] = customList[j],customList[j-1]
    print(customList)

def selectionSort(customList):
    for i in range(0,len(customList)):
        min_index = i
        for j in range(i+1,len(customList)):
            if customList[j] < customList[min_index]:
                min_index = j
        customList[i],customList[min_index] = customList[min_index],customList[i]
    print(customList)

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(0, numberOfBuckets):
        arr.append([])

    for j in customList:
        index = math.ceil(j * numberOfBuckets / maxValue)  
        arr[index - 1].append(j)
    print(arr)
    for i in range(0, numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    print(arr)

    result = []
    for i in arr:
        result.extend(i)
    print(result)


a = [1, 57, 43, 123, 99, 94, 231, 111, 78, 84, 54, 3, 33, 999]

bubbleSort(a)
selectionSort(a)
insertionSort(a)
bucketSort(a)