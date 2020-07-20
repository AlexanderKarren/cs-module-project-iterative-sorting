def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index

    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1
