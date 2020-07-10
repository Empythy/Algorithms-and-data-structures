# -*- coding: utf-8 -*-#
"""
Created on  2020/7/4  19:16 
@Project:
@Author:  liuliang
@Email:  1258644178@qq.com 
@Description:
@version: V1
"""


class ListNode():
	def __init__(self, val):
		self.val = val
		self.next = None


class Solution():
	def removeNthFromEnd(self, head, n):
		dummy = ListNode(None)
		dummy.next = head
		L = 0
		t = head
		while t:
			L += 1
			t = t.next

		L -= n
		t = dummy
		while L > 0:
			L -= 1
			t = t.next

		t.next = t.next.next

		return dummy.next


	def method2(self, head, n):
		# 快慢指针
		dummy = ListNode(None)
		dummy.next = head

		first = dummy
		second = dummy
		# 注意边界条件
		for i in range(n+1):
			first = first.next


		while first:
			first = first.next
			second = second.next

		second.next = second.next.next

		return dummy.next
