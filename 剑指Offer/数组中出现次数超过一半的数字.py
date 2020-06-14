# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        lastVal = numbers[0]
        lastCount = 1
        for item in numbers[1:]:
            if item == lastVal:
                lastCount += 1
            else:
                if lastVal == 0:
                    lastVal = item
                    lastCount = 1
                else:
                    lastCount -= 1

            if lastCount == 0:
                lastVal = 0


        """可能没有出现一半的值"""
        count = 0
        for item in numbers:
            if item == lastVal:
                count += 1
                if count > (len(numbers) >> 1):
                    return lastVal
        return 0


if __name__ == '__main__':
    # numbers = [1,2,3,2,2,2,5,4,2]
    numbers = [1,2,3,2,4,2,5,2,3]
    lastVal = Solution().MoreThanHalfNum_Solution(numbers)
    print(lastVal)
