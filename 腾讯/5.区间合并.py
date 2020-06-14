"""
小Q在进行一场竞技游戏,这场游戏的胜负关键就在于能否能争夺一条长度为L的河道,即可以看作是[0,L]的一条数轴。
这款竞技游戏当中有n个可以提供视野的道具−真视守卫,第i个真视守卫能够覆盖区间[xi,yi]。现在小Q想知道至少用几个真视守卫就可以覆盖整段河道。
"""

# n = 8
# ranges = [4, 0, 0, 0, 0, 0, 0, 0, 4]
from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        range_a_b = []
        for i in range(len(ranges)):
            if ranges[i] ==0:
                continue
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            range_a_b.append([left, right])

        sorted_a_b = sorted(range_a_b, key=lambda x: (x[0], -x[1]))

        print("sorted_a_b", sorted_a_b)

        # [[0, 6], [0, 6], [1, 7], [2, 8], [3, 9], [5, 9], [5, 7]]
        # 消除包含的区间
        # [[0, 6], [1, 7], [2, 8], [3, 9]]

        cnt = 0
        last_item = [0, 6]
        sorted_a_b_1 = [last_item]
        # last_item = [0, 6]
        for i in range(1, len(sorted_a_b)):
            cur_item = sorted_a_b[i]
            if cur_item[0] >= last_item[0] and cur_item[1] <= last_item[1]:
                continue
            sorted_a_b_1.append(cur_item)
            last_item = cur_item
        print("sorted_a_b_1=", sorted_a_b_1)


        ans = []
        tmp_range = sorted_a_b_1[0]
        if len(sorted_a_b_1) == 0:
            return -1
        if sorted_a_b_1[0][0] > 0:
            return -1
        def union(a, b):
            pass

        for item in range(1, len(sorted_a_b_1)-1):
            tmp_range = union(tmp_range, item)
















class SolutionJump:
    """
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    """
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0  # 前一次跳跃  跳的最远的位置
        max_bound = 0  # 跳的最远的位置
        for i in range(len(nums)-1):
            max_bound = max(max_bound, nums[i]+i ) # 尝试在可跳范围内 跳跃 取得最大值

            if(i == end):
                step += 1
                end = max_bound #
        return step


class Solution2:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        g = {}
        for i in range(len(ranges)):
            if ranges[i] == 0:  # 忽略坏掉的水龙头
                continue
            l = max(0, i - ranges[i])
            r = min(n, i + ranges[i])
            if r not in g.keys():
                g[r] = l
            else:
                if l < g[r]:  # 取最小左端点
                    g[r] = l

        g = [(k, v) for k, v in g.items()]
        g = sorted(g)  # 进行排序
        # print(g)

        dp = [1e4] * (n + 1)

        for r, l in g:
            if l == 0:
                dp[r] = 1
            else:
                tmp = dp[l:r]
                dp[r] = min(tmp) + 1

        return dp[n] if dp[n] < 1e4 else -1


n = 9
ranges = [0, 5, 0, 3, 3, 3, 1, 4, 0, 4]
s = Solution()
ans = s.minTaps(9, ranges)
print(ans)



