from collections import namedtuple


def test():
    # 朴素写法
    N = 1010
    f = [0] * N
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        v, w, s = map(int, input().split())
        if (s == -1):
            s = 1  # 设置物品数上限为1
        elif (s == 0):
            s = 1010  # 设置物品无限个，不超过背包体积
        for j in range(m, v - 1, -1):
            max_k = min(s, j // v)
            for k in range(max_k + 1):
                f[j] = max(f[j], f[j - k * v] + k * w)
    print(f[m])


"""
#include <iostream>
#include <vector>
using namespace std;
const int N = 1010;
int f[N];
struct Good
{
    int v, w;
};
int main()
{
    vector<Good> goods;
    int n, m; cin >> n >> m;
    for(int i = 1; i <= n; i++)
    {
        int v, w, s; cin >> v >> w >> s;
        if(s==-1) s = 1;
        else if(s==0) s = 1010;
        for(int k = 1; k <= s; k *= 2)
        {
            s -= k;
            goods.push_back({k * v, k * w});
        }
        if(s>0) goods.push_back({s * v, s * w});
    } 


    // 01背包
    for(auto good: goods)
        for(int j = m; j >= good.v; j--)
            f[j] = max(f[j], f[j - good.v] + good.w);
    cout << f[m] << endl;
    return 0;
}
链接：https://www.acwing.com/solution/acwing/content/7902/
"""


def test1():
    # 二进制优化写法
    N = 1010
    f = [0] * N
    n, m = map(int, input().split())
    goods = namedtuple("good", ["v", "w"])
    Goods = []

    for i in range(1, n + 1):
        v, w, s = map(int, input().split())
        if (s == -1):
            s = 1  # 设置物品数上限为1
        elif (s == 0):
            s = 1010  # 设置物品无限个，不超过背包体积
        k = 1
        while k <= s:
            s -= k
            Goods.append(goods._make([v * k, w * k]))
            k *= 2
        if s > 0:
            Goods.append(goods._make([v * s, w * s]))

    for good in Goods:
        for j in range(m, good.v - 1, -1):
            f[j] = max(f[j], f[j - good.v] + good.w)
    print(f[m])
