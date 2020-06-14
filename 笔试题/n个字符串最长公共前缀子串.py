def commonLength(str1, str2):
    res = 0
    while str1 and str2 and str1.pop(0) == str2.pop(0):
        res += 1
    return res


if __name__ == '__main__':
    num = int(input())
    str_list = []
    for i in range(num):
        strTmp = input()
        str_list.append(strTmp)
    try:
        while True:
            idx = input()
            if not idx:
                break
            idx = list(map(int, idx.split()))
            str1 = list(str_list[idx[0] - 1])
            str2 = list(str_list[idx[1] - 1])
            res = commonLength(str1, str2)
            print(res)
    except:
        pass