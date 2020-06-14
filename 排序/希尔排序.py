def shell_sort(arr):
    """希尔排序"""
    # 取整计算增量（间隔）值
    gap = len(arr) // 2
    while gap > 0:
        # 从增量值开始遍历比较
        for i in range(gap, len(arr)):
            j = i
            current = arr[i]
            # 元素与他同列的前面的每个元素比较，如果比前面的小则互换
            while j - gap >= 0 and current < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
        # 缩小增量（间隔）值
        gap //= 2
    return arr


"""

希尔排序的整体思想是将固定间隔的几个元素之间排序，
然后再缩小这个间隔。这样到最后数列就成为了基本有序数列，
而前面我们讲过插入排序对基本有序数列排序效果较好。
1. 计算一个增量（间隔）值 
2. 对元素进行增量元素进行比较，比如增量值为7，
那么就对0,7,14,21...个元素进行插入排序 
3. 然后对1,8,15...进行排序，依次递增进行排序
4. 所有元素排序完后，缩小增量比如为3，然后又重复上述第2，3步
 5. 最后缩小增量至1时，数列已经基本有序，最后一遍普通插入即可

已知的最增量式是由 Sedgewick 提出的 (1, 5, 19, 41, 109,...)，该步长的项来自 9 * 4^i - 9 * 2^i + 1 和 4^i - 3 * 2^i + 1 这两个算式。这项研究也表明 "比较在希尔排序中是最主要的操作，而不是交换。 用这样增量式的希尔排序比插入排序和堆排序都要快，甚至在小数组中比快速排序还快，但是在涉及大量数据时希尔排序还是比快速排序慢。

比较性：排序时元素之间需要比较，所以为比较排序
稳定性：因为希尔排序是间隔的插入，所以存在相同元素相对顺序被打乱，所以是不稳定排序
时间复杂度： 最坏时间复杂度O(n^2)平均复杂度为O(n^1.3)
空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1)
记忆方法：插入排序是每轮都是一小步，希尔排序是先大步后小步，
它第一个突破O(n2)的排序算法。联想起阿姆斯特朗登月之后说：
这是我个人一小步，却是人类迈出的一大步。
"""

if __name__ == "__main__":
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    res = shell_sort(arr)
    print(res)
