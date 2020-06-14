

def share_value(n):
    if n < 1:
        return 0
    if n <= 2:
        return n

    # 先计算第n天内跌了i次，然后价格即为 n-i-i
    tem = 2
    i = 0
    while tem < n:
        i += 1
        tem += (i + 2)

    return n - i - i

while 1:
    try:
        n = int(input())
        print(share_value(n))
    except:
        break
