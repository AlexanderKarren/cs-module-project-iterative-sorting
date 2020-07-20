def insertion_sort(input_list):
    # separate the first element
    # think of it as sorted
    # no code required / abstract step
    # for all unsorted items
    for i in range(1, len(input_list)):
        # mark the current item we are considering
        current = input_list[i]

        # look left until we find the proper place
        # to insert the current item
        j = i
        while j > 0 and current < input_list[j - 1]:

            # as we are "looking left," we need to shift
            # items to the right
            input_list[j] = input_list[j - 1]
            j -= 1

        # when we've found our insertion point (j)
        input_list[j] = current

    return input_list


print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))


# TO-DO: Complete the selection_sort() function below
# Time complexity: O(n ^ 2)
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            # if smaller than current index, update the min index
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    running = True
    while running:
        swap_made = False
        for i in range(len(arr)):
            if i < len(arr) - 1:
                if arr[i] > arr[i + 1]:
                    swap_made = True
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not swap_made:
            running = False

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


# Time complexity: O(n+k)
def counting_sort(arr, maximum=None):
    # Your code here

    return arr
