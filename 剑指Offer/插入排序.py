def insertion_sort(arr):
    """插入排序"""
    # 第一层for表示循环插入的遍数
    for i in range(1, len(arr)):
        # 设置当前需要插入的元素
        current = arr[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            arr[pre_index + 1] = arr[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
        # 当比较元素小于当前元素，则将当前元素插入在 其后面
        arr[pre_index + 1] = current
    return arr


"""
插入排序的适用场景：一个新元素需要插入到一组已经是有序的数组中，
或者是一组基本有序的数组排序。
1. 比较性：排序时元素之间需要比较，所以为比较排序 
2. 稳定性：从代码我们可以看出只有比较元素大于当前元素，比较元素才会往后移动，
            所以相同元素是不会改变相对顺序 
3. 时间复杂度：插入排序同样需要两次循坏一个一个比较，故时间复杂度也为O(n^2) 
4. 空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1) 
5. 记忆方法：想象成在书架中插书：先找到相应位置，将后面的书往后推，再将书插入
"""