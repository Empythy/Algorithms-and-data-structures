# def bubble_sort(arr):
#     # 第一层for表示循环的遍数
#     for i in range(len(arr)):
#         # 第二层for表示具体比较哪两个元素
#         for j in range(len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#             # if compare(arr[j], arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#         return arr
# 遍历所有数组元素


"""
冒泡排序是一种简单直接暴力的排序算法，为什么说它暴力？因为每一轮比较可能多个元素移动位置，
而元素位置的互换是需要消耗资源的，所以这是一种偏慢的排序算法，
仅适用于对于含有较少元素的数列进行排序。
稳定性：我们从代码中可以看出只有前一个元素大于后一个元素才可能交换位置，
    所以相同元素的相对顺序不可能改变，所以它是稳定排序
比较性：因为排序时元素之间需要比较，所以是比较排序
时间复杂度：因为它需要双层循环n*(n-1))，所以平均时间复杂度为O(n^2)
空间复杂度：只需要常数个辅助单元，所以空间复杂度为O(1)，
        我们把空间复杂度为O(1)的排序成为原地排序（in-place）
记忆方法：想象成气泡，一层一层的往上变大
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # if arr[j] > arr[j + 1]:
            if not compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort1(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def compare(str1, str2):
    """str1 是否大于str2 """
    if len(str1.strip()) == 0:
        return True
    if len(str2.strip()) == 0:
        return False
    min_len = min(len(str1), len(str2))

    for i in range(min_len):
        if str1[i] == str2[i]:
            i += 1
            continue
        elif str1[i] > str2[i]:
            return True
        else:
            return False
    if len(str1) < len(str2):
        return True
    else:
        return False


if __name__ == "__main__":
    # input_data = input()
    input_data = "waimai,dache,lvyou,liren,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian"
    # waimai,menpiao,meishi,lvyou,lvyoujingdian,liren,jiudian,jiehun,jiaopei,dache
    # ['waimai', 'meishi', 'menpiao', 'lvyou', 'liren', 'lvyoujingdian', 'jiudian', 'jiaopei', 'jiehun', 'dache']

    str_list = input_data.split(",")
    ret = bubble_sort(str_list)
    print(ret)
    print(compare('meishi', 'menpiao'))
    import random

    print(bubble_sort1([random.randint(0, 10) for _ in range(10)]))







































