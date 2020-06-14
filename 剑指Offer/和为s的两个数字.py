# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here

        if len(array) < 1 or sum(array) < tsum:
            return None
        left = 0
        right =len(array)-1
        ret = []
        while left < right:
            tmpSum = array[left] + array[right]
            if tmpSum == tsum:
                ret.append([array[left], array[right]])
                left += 1
                right -= 1
            elif tmpSum > tsum:
                right -= 1
            else:
                left += 1

        ret.sort(key=lambda x: x[0]*x[1])
        return ret[0][0] * ret[0][1]


if __name__ == '__main__':
    array = [1, 2, 4, 4 ,7, 11, 11, 15]
    num = 15
    s = Solution()
    s.FindNumbersWithSum(array, num)

