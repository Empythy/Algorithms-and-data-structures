# -*- coding:utf-8 -*-
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，
当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if len(s) == 0:
            return ""
        length = len(s)
        space_cnt = s.count(" ")
        new_s = ["0"] * (length + 2 * space_cnt)
        new_s_index = length + 2 * space_cnt - 1
        for i in range(length - 1, -1, -1):
            if s[i] != " ":
                new_s[new_s_index] = s[i]
                new_s_index -= 1
            else:
                new_s[new_s_index] = "0"
                new_s[new_s_index - 1] = "2"
                new_s[new_s_index - 2] = "%"
                new_s_index -= 3
        return "".join(new_s)


s = Solution()
print(s.replaceSpace("We Are Happy."))
