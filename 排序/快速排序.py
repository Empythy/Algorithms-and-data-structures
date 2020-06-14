def qsort(arr):

    if len(arr) <=1:
        return arr
    povit = arr[0]

    left = [item for item in arr if item < povit]
    right = [item for item in arr if item >= povit]
    return qsort(left) + povit + qsort(right)


