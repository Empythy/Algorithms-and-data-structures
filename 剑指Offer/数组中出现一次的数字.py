"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ## 如果两个数字相同  异或操作为0
        ## a ^ b ^ c = a ^ c ^ b
        if len(array) < 2:
            return None
        twoNumXor = None
        for num in array:
            if twoNumXor == None:
                twoNumXor = num
            else:
                twoNumXor = twoNumXor ^ num
        # 找出哪一位不一样
        count = 0
        while twoNumXor % 2 == 0:
            twoNumXor = (twoNumXor>> 1)
            count += 1

        mask = (1 << count)
        firstNum = None
        secondNum = None
        for num in array:
            if mask & num == 0:
                if firstNum == None:
                    firstNum =num
                else:
                    firstNum = firstNum ^ num
            else:
                if secondNum == None:
                    secondNum =num
                else:
                    secondNum = secondNum ^ num
        return [firstNum, secondNum]







