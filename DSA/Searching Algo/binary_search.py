def binarySearch(array, value):
    start = 0
    end = len(array)-1
    mid = (start+end)//2
    while array[mid] != value and start<=end:
        if value < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start+end)//2
    if array[mid] == value:
        return mid
    else:
        return -1
    
a = [3, 5, 34, 35, 44, 123]
print(binarySearch(a, 123))
