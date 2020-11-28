def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lesser = [i for i in range(array[1:]) if i < pivot]
        greater = [i for i in range(array[1:]) if i > pivot]
        return quicksort(lesser) + pivot + quicksort(greater)
