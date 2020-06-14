"""给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串。

输入: S = "aab"
输出: "aba"
输入: S = "aaab"
输出: ""


1. 统计所有字符串对应的个数  若最多的字母超过一半+2 则不满足条件
2.
"""
from collections import Counter
from operator import itemgetter


def demo():
    S = "aab"
    s = sorted(S)
    count = Counter(S)
    s.sort(key=count.get)
    print("sorted s is ", s)
    # s = ['b', 'a', 'a']
    sorted_s = sorted(count.items(), key=itemgetter(1))
    print(sorted_s)
    n = len(s) // 2  # n=1
    a, b = sorted_s[:n], s[n:]
    if s[n - 1] == s[-1]:
        print('')
    for i in range(len(b)):
        s[i * 2] = b[i]
    for i in range(len(a)):
        s[i * 2 + 1] = a[i]

    print(''.join(s))
