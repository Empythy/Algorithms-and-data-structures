"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""

# -*- coding:utf-8 -*-
import itertools
"""
理解函数: itertools.permutations()
"""
class Solution:
     def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                ## 如果后一个字符和前一个字符相等 则跳出
                continue
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr


if __name__ == '__main__':
    s = Solution()
    ret = s.Permutation("aab")
    print(ret)
