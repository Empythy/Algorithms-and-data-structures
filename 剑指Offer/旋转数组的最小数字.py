"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
if |mid - left | < |mid - right|  右边
"""
# -*- coding:utf-8 -*-
class Solution:
    # def minNumberInRotateArray(self, rotateArray):
    #     write code here
        # for i in range(0, len(rotateArray)):
        #     minNum = minNum if minNum<rotateArray[i] else rotateArray[i]
        # return minNum

    def minNumberInRotateArray(self, rotateArray):
        # 最小值一定比前面的值小
        # 二分法查找数据 找左右的方法是 |mid - left | < |mid - right|
        # 右边的值大于中指 就说明最小值在左边， 否则在右边
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            mid = (left + right) >> 1
            if rotateArray[mid] < rotateArray[mid-1]:
                return rotateArray[mid]
            elif rotateArray[mid] < rotateArray[right]:
                right = mid - 1
            else:
                left = mid + 1

        return 0








