from functools import lru_cache

"""
1
3 1
1 2 5
10 11 6
12 12 7
"""
def solution(n, k, A):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = [float("-inf")]
    used = [[False] * n for _ in range(n)]   # 注意初始化数组   [[False] * n] * n  不能直接这样初始化
    @lru_cache(None)  # 有递归 
    def dfs(track, row, col):
        for i in range(1, k + 1):
            for tx, ty in d:
                new_row = row + i * tx
                new_col = col + i * ty

                if 0 <= new_row < n and 0 <= new_col < n and \
                        not used[new_row][new_col] and \
                    A[new_row][new_col] > A[row][col]:

                    used[new_row][new_col] = True
                    dfs(track + (A[new_row][new_col],), new_row, new_col)
                    used[new_row][col] = False
                else:
                    # print(track)
                    # print(used)
                    res[0] = max(res[0], sum(track))
    track = (A[0][0],)  #  注意 初始位置
    used[0][0] = True
    dfs(track, 0, 0)
    print(max(res))

if __name__ == "__main__":
    # T = int(input())
    # for line in range(T):
    #     line1 = input().split()
    #     n, k = int(line1[0]), int(line1[1])
    #     data = []
    #     for i in range(n):
    #         data_line = input().split(" ")
    #         data.append([int(item) for item in data_line])
    #         solution(n, k, data)
    n, k = 3, 1
    # A = [[1, 2, 5],
    #      [10, 11, 6],
    #      [12, 12, 7]]
    A = [[1, 10, 11],
         [2, 11, 12],
          [5,6,  7]]
    solution(n, k, A)