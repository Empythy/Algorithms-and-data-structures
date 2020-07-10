# -*- coding: utf-8 -*-#
"""
Created on  2020/7/6  13:49 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


def rand5():
    pass


def rand7():
    while True:
        x = (rand5() - 1) * 5 + rand5()
        if x <= 21:
            return x % 3 + 1

def rand3():
    while True:
        x = rand5()
        if x <= 3:
            return x