"""
众所周知，美团外卖的口号是:”美团外卖,送啥都快”。身着黄色工作服的骑手作为外卖业务中商家和客户的重要纽带，
，以快速送餐突出业务能力；工作之余，他们会通过玩智力游戏消遣闲暇时光，以反应速度彰显智慧
，每位骑手拿出装有货物的保温箱，参赛选手需在最短的时间内用最少的保温箱将货物装好。
我们把问题简单描述一下:
1 每个货物占用空间都一模一样
2 外卖小哥保温箱的最大容量是不一样的,每个保温箱由两个值描述: 保温箱的最大容量 bi ,当前已有货物个数 ai ,(ai<=bi)
3 货物转移的时候,不必一次性全部转移,每转移一件货物需要花费 1秒 的时间
"""
# import copy
#
# n = int(input().strip())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# b_tmp = copy.deepcopy(b)
# b_tmp.sort()
# bb = []  # 存储最大的k个b_i
# for i in range(n):
#     bb.append(b_tmp[n - 1 - i])
#     if sum(bb) >= sum(a):
#         break
# k = i + 1
# count = 0
# aa = []  # 存储符合选中b_i的a_i：>=k个
# len_aa = len(aa)
# for i in range(n):
#     if b[i] in bb:
#         aa.append(a[i])
# for i in range(len(bb)):
#     if (bb[-1] == bb[len(bb) - 1 - i]):
#         count += 1
# a_last = []
# for i in range(n):
#     if b[i] == bb[-1]:
#         a_last.append(a[i])
#         del aa[aa.index(a[i])]  # 删掉了 所以aa有重复的也没事
# a_last.sort()
# a_last = a_last[0:count]
# t = sum(a) - sum(aa) - sum(a_last)
# print(k, t)


def resolve(a, b):
    # new_b = list(zip(b, range(len(b))))
    # print(f"a={a}")
    # print(f"b={b}")
    b_a_pair = list(zip(a, b))
    # print(f"b_a_pair={b_a_pair}")
    b_a_pair.sort(key=lambda item:item[1], reverse=True)
    # print(f"sorted b_a_pair={b_a_pair}")
    new_a = [item[0] for item in b_a_pair]
    new_b = [item[1] for item in b_a_pair]
    # print(f"new_b:{new_b}")
    # print(f"new_a:{new_a}")
    sum_a = sum(new_a)

    i = 0
    tmp_b_sum = 0
    while i < len(new_b):

        tmp_b_sum += new_b[i]
        # print(f"i={i}, sum_a={sum_a}, tmp_b_sum={tmp_b_sum}")
        if tmp_b_sum >= sum_a:
            # print(i, tmp_b_sum, sum_a)
            break
        i += 1
    return (str(i+1), str(sum(new_a[i+1:])))

if __name__ == "__main__":
    n = int(input().strip())
    input_data1_list = ["3 3 4 3", "1 1", "10 30 5 6 24", "1 1"]
    input_data2_list = ["4 7 6 5", "100 100", "10 41 7 8 24", "1 1"]
    for input_data1, input_data2 in zip(input_data1_list, input_data2_list):
        # input_data1 = input().split()
        input_data1 = input_data1.split()
        a =[int(item) for item in input_data1]
        input_data2 = input_data2.split()
        # input_data2 = input().split()
        b = [int(item) for item in input_data2]
        ret = resolve(a, b)
        print(" ".join(ret))
        print("=" * 30)

