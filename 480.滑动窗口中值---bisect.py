import bisect
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        My solution, using sorted list
        Time: O(nlog(k))
        Space: O(n+k)
        """
        res = []
        if not nums or not k:
            return res
        def append_median():
            if k % 2 == 1:
                median = sorted_list[k // 2]
            else:
                median = (sorted_list[k // 2] + sorted_list[k // 2 - 1]) / 2
            res.append(median)

        n = len(nums)
        p1, p2 = 0, k
        sorted_list = sorted(nums[p1:p2])
        append_median()

        while p2 != n:
            # 先插入 下一个值
            bisect.insort(sorted_list, nums[p2])
            #  bisect.insort说明
            #  Insert item x in list a, and keep it sorted assuming a is sorted.
            #  If x is already in a, insert it to the right of the rightmost x.
            # 查找左边有少个数字小于等于x
            del_index = bisect.bisect(sorted_list, nums[p1])
            # bisect.bisect
            #  Return the index where to insert item x in list a, assuming a is sorted.
            #  The return value i is such that all e in a[:i] have e <= x, and all e in
            #   a[i:] have e > x.  So if x already appears in the list, i points just
            #   beyond the rightmost x already there
            # 主要找到的索引需要 - 1
            del sorted_list[del_index - 1]
            append_median()

            p1 += 1
            p2 += 1

        return res
