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


a = [1,57,43,123,12]

bubbleSort(a)
selectionSort(a)