import sys


def height_compute(key):
    try:
        return height_compute(input_dict[key]) + 1
    except KeyError:
        return 1


n = int(input().strip())
if n == 1:
    print(1)
else:
    input_dict = {}
    count = 1
    while count < n:
        s1 = sys.stdin.readline().strip()
        if s1 == '':
            break
        s = list(map(int, s1.split()))
        input_dict[s[1]] = s[0]
        count += 1
    child_list = list(input_dict.keys())
    res = []
    for key in child_list:
        height = height_compute(key)
        res.append(height)
    print(max(res))