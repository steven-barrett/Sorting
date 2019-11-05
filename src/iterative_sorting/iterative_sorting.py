# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        ele = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = ele

    return arr


newArr = [4, 6, 3, 1, 9, 2, 7, 8]
selection_sort(newArr)
print(newArr)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    # Setting the range for comparison (first round: n, second round: n-1  and so on)
    for i in range(len(arr)-1, 0, -1):

        for j in range(i):
            # Compare element with its right side neighbor
            if arr[j] > arr[j+1]:

                # swap them
                ele = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = ele

    return arr


print(bubble_sort([5, 1, 2, 3, 9, 8, 0]))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
