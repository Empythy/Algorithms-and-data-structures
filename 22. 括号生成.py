from typing import List


class Solution:
    def is_vilid(self, path):
        if path[0] == ')':
            return False
        stack = ['?']
        for i in range(len(path)):
            if path[i] == '(':
                stack.append('(')
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def  backtrack(path, n_left, n_right):
            if len(path) == 2 * n:
                ans.append(path.copy())
                return
            if n_left > 0 and self.is_vilid(path + ['(']):
                backtrack(path+['('], n_left-1, n_right)
            if n_right > 0 and self.is_vilid(path + [')']):
                backtrack(path + ['('], n_left, n_right-1)

        backtrack([], n, n)
        return ans
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''
        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                # 满足条件
                res.append(cur_str)
                return

            if right < left:
                return
            # 做选择

            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res


str1 = '())'
s = Solution()
assert s.is_vilid(str1) == True


str1 = ')('
s = Solution()
assert s.is_vilid(str1) == False