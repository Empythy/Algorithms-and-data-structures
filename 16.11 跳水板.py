# -*- coding: utf-8 -*-#
"""
Created on  2020/6/12  16:23 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""

# 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
#
# 返回的长度需要从小到大排列。
# 输入：
# shorter = 1
# longer = 2
# k = 3
# 输出： {3,4,5,6}
#

from functools import lru_cache
from typing import List

# 1
# 1
# 100000


class Solution:
    @lru_cache(None)
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if shorter == longer:
            return [ k * shorter]

        if k==0:
            return []
        short_subprob = self.divingBoard(shorter, longer, k-1)
        longer_subprob = self.divingBoard(shorter, longer, k-1)

        if short_subprob:
            short_sub = [shorter + _ for _ in short_subprob]
        else:
            short_sub = [shorter, ]


        if longer_subprob:
            longer_sub = [longer + _ for _ in longer_subprob]
        else:
            longer_sub = [longer, ]

        res = list(set(short_sub + longer_sub))
        res.sort()
        return res


s = Solution()
res = s.divingBoard(7, 3625, 19808)
print(res)