import numpy as np

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

def c_list(n, x, y):
    c = []
    x = np.array(x)
    y = np.array(y)
    for i in range(n):
        # print(x[:i+1])
        midx, midy = np.sum(x[:i + 1]) // (i + 1), np.sum(y[:i + 1]) // (i + 1)
        c_i = np.sum(np.fabs(x[:i + 1] - midx) + np.fabs(y[:i + 1] - midy))
        c.append(c_i)
    return c


for i in c_list(n, x, y):
    print(int(i), end=' ')
