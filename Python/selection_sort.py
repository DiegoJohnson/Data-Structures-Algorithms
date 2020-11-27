
def findSmallest(arr):
    index = 0 

    for i in range(1, len(arr)):
        if arr[i] < arr[index]:
            index = i
    return index

def selectionSort(arr):
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        arr.append(arr.pop(smallest))

    return arr