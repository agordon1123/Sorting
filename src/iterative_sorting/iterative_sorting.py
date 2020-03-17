import traceback
# for line in traceback.format_stack():
#     print(line.strip())

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        while smallest_index != len(arr):
            if arr[cur_index] > arr[smallest_index]:
                # TO-DO: swap
                arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
            smallest_index += 1

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # set swapped to false at each outer loop
        swapped = False

        for j in range(0, len(arr) - 1):
            left = j
            right = j + 1
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
                # a value was swapped on this pass
                swapped = True

        # return array once sorted
        if swapped != True:
            return arr
    # return if n=0
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum = -1):
    # check for correct input
    if not len(arr):
        return []
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    # find largest number
    maximum = max(arr)
    # create counted arr for indeces to hold count of vars
    counted = [0] * (maximum + 1)
    # create final array
    final = []

    # fill counted arr indeces with count of vars
    for i in range(len(arr)):
        counted[arr[i]] = arr.count(arr[i])

    total = 0
    # create cumulative count of vars through indeces
    for i in range(len(counted)):
        total += counted[i]
        counted[i] = total

    iterator = 0
    # loop through and append indeces where count increases
    for i in range(len(counted)):
        if counted[i] != iterator:
            num = counted[i] - iterator
            while num > 0:
                final.append(i)
                num -= 1
            iterator = counted[i]

    return final
    # return arr