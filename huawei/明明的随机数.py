while True:
    try:
        arr = []
        n = int(input())
        for i in range(n):
            arr.append(int(input()))
        arr_set = list(set(arr))
        arr_set.sort()
        for item in arr_set:
            print(str(item))
    except:
        break