"""
小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。

小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？

（当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住）
输入第一行将包含一个数字n，代表楼的栋数，接下来的一行将包含n个数字wi(1<=i<=n)，代表每一栋楼的高度。
1<=n<=100000;
1<=wi<=100000;

6
5 3 8 3 2 5

"""

# 5 3 8 3 2 5
# 3 3 5 4 4 4
# 当小Q处于位置3时，他可以向前看到位置2,1处的楼，向后看到位置4,6处的楼，
# 加上第3栋楼，共可看到5栋楼。当小Q处于位置4时，
# 他可以向前看到位置3处的楼，向后看到位置5,6处的楼，加上第4栋楼，共可看到4栋楼。
def look_after(w):
    """
    往后看 能看见多少楼
    :param w:
    :return:
    """
    stack = [w[-1]] # 升序的栈
    ans = [0]
    for i in range(n-2, -1, -1):
        ans.append(len(stack)) # 根据栈的长度
        while stack and w[i] >= stack[-1]: # 如果当前的楼层比栈顶高 就pop
            stack.pop()
        stack.append(w[i])
    return ans[::-1]


n = int(input())
w = list(map(int, input().split()))

ans1 = look_after(w)
new_w = w.copy()[::-1]
ans2 = look_after(new_w)
ans = []
for item1, item2 in zip(ans1, ans2[::-1]):
    ans.append(str(item1 + item2 + 1))
ans = " ".join(ans)

print(ans)
# assert ans == "3 3 5 4 4 4"



"""
您的代码已保存
请检查是否存在语法错误或者数组越界非法访问等情况
case通过率为0.00%
"""
