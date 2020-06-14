from bisect import bisect

def bisearch(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) >> 1
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        # elif arr[mid] == num:
        #     return mid
    return left



#查找数字的左边界
def left_bound(arr, num):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) >> 1
        if arr[mid] == num:
            right = mid
        elif arr[mid] > num:
            right = mid
        elif arr[mid] < num:
            left = mid + 1
    # 比所有数都大
    print(left)
    if left == len(arr): return -1
    return left if arr[left] == num else -1


def right_bound(arr, num):

    if (len(arr) == 0): return -1
    left = 0
    right = len(arr)
    while (left < right) :
        mid = (left + right) // 2
        if (arr[mid] == num):
            left = mid + 1 #注意
        elif (arr[mid] < num):
            left = mid + 1
        elif (arr[mid] > num):
            right = mid
    # return left - 1  # 注意
    if left == 0: return -1
    return left - 1 if arr[left-1] == num else-1

arr = [1, 2, 3, 4, 4, 5]
res = left_bound(arr, 1.5)

print(res)