
class Solution(object):
    def solveNQueen(self, n):
        ans = []
        def dfs(nums, row):
            """nums数组第i个元素存放col"""
            if row == n:
                ans.append(nums[:])
                return
            for col in range(n):
                nums[row] = col  # 隐含了撤销上一次选择
                if vilid(nums, row): # 判断选择是否合理
                    dfs(nums, row+1)

        def vilid(nums, row):
            for i in range(row):  #指前面的行
                if nums[i] == nums[row] or abs(nums[i] - nums[row]) == abs(i-row):
                    return False
            return True

        dfs([None for _ in range(n)], 0)
        ret = [[] for _ in range(len(ans))]
        tmp = "." * n
        for i in range(len(ans)):
            for col in ans[i]:
                ret[i].append(tmp[:col] + "Q" + tmp[col+1:])
        return ret

if __name__ == '__main__':
    s = Solution()
    ret = s.solveNQueen(8)
    import pprint
    pprint.pprint(ret)




