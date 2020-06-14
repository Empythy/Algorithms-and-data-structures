# -*- coding:utf-8 -*-
import random


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # return data.count(k)
        # index = self.find(data, k)
        # if index == -1:
        #     return None
        # return self.findLeft(data[:index], k) + self.findRight(data[index:],k)
        return self.biSearch(data, k + 0.5) - self.biSearch(data, k - 0.5)

    def GetNumberOfK1(self, data, k):
        # write code here
        index = self.find(data, k)
        if index == -1:
            return None
        leftLen = self.findLeft(data[:index], k)
        rightLen = self.findRight(data[index:], k)
        return leftLen + rightLen

    def biSearch(self, data, num):
        s = 0
        e = len(data) - 1
        while s <= e:
            mid = (e - s) // 2 + s
            if data[mid] < num:
                s = mid + 1
            elif data[mid] > num:
                e = mid - 1
        return s

    def find(self, data, k):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) >> 1
            if data[mid] == k:
                return mid
            elif data[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def findLeft(self, data, k):

        if len(data) == 0 or data[-1] != k:
            return 0
        if data[0] == data[-1]:
            return len(data)
        left = 0
        right = len(data) - 1
        k = data[-1]
        while left <= right:
            mid = (left + right) >> 1
            if data[mid] == k:
                right = mid
            else:
                left = mid

            if right - left == 1:
                return len(data) - left - 1

    def findRight(self, data, k):
        if data[0] != k:
            return 0
        if data[0] == data[-1]:
            return len(data)
        left = 0
        right = len(data) - 1
        k = data[0]
        while left <= right:
            mid = (left + right) >> 1
            if data[mid] == k:
                left = mid
            else:
                right = mid

            if right - left == 1:
                return right

    def GetNumberOfK2(self, data, k):
        # write code here
        return self.getUpper(data, k) - self.getLower(data, k) + 1

    def getLower(self, data, k):
        start, end = 0, len(data) - 1
        mid = (start + end) // 2
        while start <= end:
            if data[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) // 2
        return start

    def getUpper(self, data, k):
        start, end = 0, len(data) - 1
        mid = (start + end) // 2
        while start <= end:
            if data[mid] <= k:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) // 2
        return end


if __name__ == '__main__':
    # data = [0,1,2,4,4,5,5, 5, 5, 5, 5, 5, 5, 5]

    s = Solution()
    s.getUpper([5, 5, 5, 5, 5, 5, 5, 5, 5, 6], 5)

    """
   
    
    data = [0, 2, 2, 2, 2, 3, 5, 5, 5, 5]
    k = 0
    """
    # data = [0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5]
    # k = 2
    # ret = s.GetNumberOfK1(data, k)
    # print(ret)
    # for _ in range(20):
    #     data = sorted([random.randint(0, 5) for _ in range(20)])
    #     k = random.randint(0, 9)
    #     print(data, "\t", data[k])
    #     ret = s.GetNumberOfK1(data, data[k]) == data.count(data[k])
    #     print("个数为", ret)

"""
[0, 1, 1, 1, 1, 2, 4, 4, 4, 5] 	 5
[0, 2, 2, 2, 2, 3, 5, 5, 5, 5] 	 0
[0, 0, 0, 1, 3, 4, 4, 4, 4, 5] 	 5
[0, 1, 1, 1, 2, 2, 3, 3, 5, 5] 	 0

"""
