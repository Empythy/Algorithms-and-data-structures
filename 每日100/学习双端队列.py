from collections import deque
"""
https://docs.python.org/zh-cn/3.7/tutorial/stdlib2.html?highlight=deque
collections 模块提供了一种 deque() 对象，它类似于列表，但从左端添加和弹出的速度较快，而在中间查找的速度较慢。 
此种对象适用于实现队列和广度优先树搜索
在替代的列表实现以外，标准库也提供了其他工具，例如 bisect 模块具有用于操作排序列表的函数
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
heapq 模块提供了基于常规列表来实现堆的函数。 最小值的条目总是保持在位置零。 
这对于需要重复访问最小元素而不希望运行完整列表排序的应用来说非常有用:
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
"""

d = deque()
# 往右添加一个元素
d.append(1)
d.append(2)
print(d)

# 往左边添加一个元素
d.appendleft(2)
print(d)

# 清空对列
d.clear()
print(d)
# count(返回指定元素的出现次数)
import collections

d = collections.deque()
d.append(1)
d.append(1)
print(d.count(1))

# extend 从队列右边扩展一个列表的元素
d = collections.deque()
d.append(1)
d.extend([3, 4, 5])
print(d)

# extendleft
d = collections.deque()
d.append(1)
d.extendleft([3, 4, 5])
print(d)

d = collections.deque()
d.extend(['a', 'b', 'c', 'd', 'e'])
print(d)
print(d.index('e'))
print(d.index('c', 0, 3))  # 指定查找区间

# insert（在指定位置插入元素）
d = collections.deque()
d.extend(['a','b','c','d','e'])
d.insert(2,'z')
print(d)
#输出：deque(['a', 'b', 'z', 'c', 'd', 'e'])

# pop（获取最右边一个元素，并在队列中删除）
import collections
d = collections.deque()
d.extend(['a','b','c','d','e'])
x = d.pop()
print(x,d)

#输出：e deque(['a', 'b', 'c', 'd'])

import collections
d = collections.deque()
d.extend(['a','b','c','d','e'])
d.remove('c')
print(d)

#输出：deque(['a', 'b', 'd', 'e'])



d = collections.deque()
d.extend(['a','b','c','d','e'])
d.rotate(2)   #指定次数，默认1次
print(d)

#输出：deque(['d', 'e', 'a', 'b', 'c'])