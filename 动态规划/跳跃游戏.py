"""enum Index {
    GOOD, BAD, UNKNOWN
}

public class Solution {
    Index[] memo;
    public boolean canJumpFromPosition(int position, int[] nums) {
        if (memo[position] != Index.UNKNOWN) {
            return memo[position] == Index.GOOD ? true : false;
        }

        int furthestJump = Math.min(position + nums[position], nums.length - 1);
        for (int nextPosition = position + 1; nextPosition <= furthestJump; nextPosition++) {
            if (canJumpFromPosition(nextPosition, nums)) {
                memo[position] = Index.GOOD;
                return true;
            }
        }

        memo[position] = Index.BAD;
        return false;
    }

    public boolean canJump(int[] nums) {
        memo = new Index[nums.length];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = Index.UNKNOWN;
        }
        memo[memo.length - 1] = Index.GOOD;
        return canJumpFromPosition(0, nums);
    }
}
"""

from typing import List


class Solution:


    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        self.memo = [0] * n
        # 0-->unknown 1--> bad 2-->good
        self.memo[n - 1] = 2
        return self.canJumpFromPosition(0, nums)
    def canJumpFromPosition(self, position, nums):

        if (self.memo[position] != 0):
            return True if self.memo[position]==2 else False
        furthestJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position + 1, furthestJump+1):
            if (self.canJumpFromPosition(nextPosition, nums)):
                self.memo[position] = 2
                return True
        self.memo[position] = 1
        return False

    def canJump2(self, nums: List[int]) -> bool:
        """
        超时
        :param nums:
        :return:
        """
        from functools import lru_cache
        @lru_cache(None)
        def canJumpFromPosition(position, nums):
            if (position == len(nums) - 1):
                return True
            furthestJump = min(position + nums[position], len(nums) - 1)
            for nextPosition in range(position + 1, furthestJump + 1):
                if (canJumpFromPosition(nextPosition, nums)):
                    return True
            return False

        return canJumpFromPosition(0, tuple(nums))