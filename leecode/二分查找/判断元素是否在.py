def bisearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            return mid

    return -1


def bisearch_left(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            right = mid

    if left == len(arr):
        return -1
    return left if arr[left] == target else -1


def bisearch_right(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        elif arr[mid] == target:
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1

    if (left == 0): return -1
    return (left - 1) if arr[left - 1] == target else -1
