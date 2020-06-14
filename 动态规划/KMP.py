


def search(pat, txt):
    m = len(pat)
    n = len(txt)

    for i in range(0, n-m):
        for j in range(m):
            if pat[j] != txt[i+j]:
                break
            if j == m:
                return i
    return False



