# -*- coding:utf-8 -*-
import sys
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here

        line = list(s)
        for i in range(len(line)):
            if line.count(line[i]) == 1:
                return i

if __name__ == '__main__':
    s = Solution()
    ret =s.FirstNotRepeatingChar("google")
    print(ret)
