
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    l_one = len(arrA)
    l_two = len(arrB)

    res = []
    i, j = 0, 0

    while i < l_one and j < l_two:
        if arrA[i] < arrB[j]:
            res.append(arrA[i])
            i += 1

        else:
            res.append(arrB[j])
            j += 1

    res = res + arrA[i:] + arrB[j:]

    return res

l1 = [1, 3, 5, 7, 8, 9]
l2 = [2, 4, 6, 10, 12]
print(merge(l1, l2))

# TO-DO: implement the Merge Sort function below USING RECURSION

def partition(l):
    lft = []
    pvt = l[0]
    rgt = []

    for v in l[1:]:
        if v <= pvt:
            lft.append(v)
        else:
            rgt.append(v)
    return lft, pvt, rgt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left, pivot, right = partition(arr)

    return merge_sort(left) + [pivot] + merge_sort(right)


data = [5, 9, 3, 7, 2, 8, 1, 6]
print('RECURSIVE', merge_sort(data))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
