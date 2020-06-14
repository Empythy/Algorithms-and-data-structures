from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n
        # l_max[i] 代表左边最高的柱子的高度
        # r_max[i] 代表右边最高的柱子的高度
        l_max[0] = height[0]

        for i in range(1, n):
            if height[i] > l_max[i - 1]:
                l_max[i] = height[i]
            else:
                l_max[i] = l_max[i - 1]
        r_max[-1] = height[-1]

        for i in range(n - 2, -1, -1):
            if height[i] > r_max[i + 1]:
                r_max[i] = height[i]
            else:
                r_max[i] = r_max[i + 1]
        print(l_max)
        print(r_max)
        cnt = 0
        for i in range(n):
            cnt += min(l_max[i], r_max[i]) - height[i]
        return cnt


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(height)
    solution = Solution()
    res = solution.trap(height)
    print(res)
