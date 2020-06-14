from typing import List


class Solution:
    """
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    链接：https://leetcode-cn.com/problems/jump-game-ii
    """
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        cur_max_index = nums[0]
        pre_max_index = nums[0]
        jump_min = 1
        for i in range(1, len(nums)):
            if i > cur_max_index:
                jump_min += 1  # 若无法向前移动 才进行跳跃
                cur_max_index = pre_max_index # 更新当前可达的最远的位置
            if pre_max_index < nums[i] + i:
                pre_max_index = nums[i] + i # 更新 pre_max
        return jump_min