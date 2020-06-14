# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        l = s.split(' ')
        return ' '.join(l[::-1])
class Solution1(object):
    def ReverseSentence(self, s):
        l = s.split(' ')
        l.reverse()
        return ' '.join(l)