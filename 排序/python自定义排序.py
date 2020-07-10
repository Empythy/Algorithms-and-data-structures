# -*- coding: utf-8 -*-#
"""
Created on  2020/6/29  22:03 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""
from collections import UserDict


class Envelope(object):
	"""
	实现自定义比较 对于两个对象 o1 o2
	如果 o1.w < o2.w: 返回True
		 o1.w > o2.w: 返回False
	如果 o1.w == o2.w 取决于 两者w的大小关系
		若 o1.h > o2.h: 返回True
		否则 返回False
	"""
	def __init__(self, w, h):
		self.w = w
		self.h = h

	def __lt__(self, other):
		if self.w == other.w:
			return self.h > other.h
		return self.w < other.w


o1 = Envelope(1, 2)
o2 = Envelope(1, 1)
print(o1 == o2)


UserDict
