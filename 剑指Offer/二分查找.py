def bSearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) >> 1
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return False


if __name__ == '__main__':
    ret = bSearch([1, 2, 3, 4, 5, 6, 7], 1)
    print(ret)
