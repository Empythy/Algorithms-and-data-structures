from collections import deque
from typing import List


class Solution:
    """
    在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，
    气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，
    因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。
    一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，
    若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足
     xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。
    弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
    链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_pts = deque(sorted(points, key=lambda x: (x[0], x[1])))
        res = 0
        while sorted_pts:
            pt = sorted_pts.popleft()
            res += 1
            pt_right = pt[1]
            # 注意边界条件
            while sorted_pts and pt_right >= sorted_pts[0][0]:  # 右端点大于下一个左端点
                pt_right = min(pt_right, sorted_pts[0][1])  # 更新右端点
                sorted_pts.popleft()
        return res


# l = [[10,16], [2,8], [1,6], [7,12]]
# l = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
l = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
s = Solution()

res = s.findMinArrowShots(l)
print(res)
