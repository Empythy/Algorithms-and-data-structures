"""
输出一个字符串，代表解压后的字符串。



HG[3|B[2|CA]]F  --> HGBCACABCACABCACAF
HG[3|B[2|CA]]F−>HG[3|BCACA]F−>HGBCACABCACABCACAF
"""
def decode(s):
    n = len(s)
    left = None
    right = None

    for i in range(n):
        if s[i] == '[':
            left = i
        elif s[i] == ']':
            right = i
            break
    if not left is None and not right is None:
        mid = s[left+1:right]
        print(f"mid = {mid}")
        times, t_s = mid.split('|')
        new_s = s[:left] + t_s * int(times) + s[right+1:]
        print(f"new_s = {new_s}")
        return decode(new_s)
    else:
        return s

# str_in = 'HG[3|B[2|CA]]F'
# ans = decode(str_in)
# assert ans == "HGBCACABCACABCACAF"
# str_in = "B[2|DAS]W[2|S]DQ"
# ans = decode(str_in)
# assert ans == "BDASDASWSSDQ"

str_in = "[14|FSFVSW]FSFA[3|SDFSF[8|SFSF]FSF]"

ans = decode(str_in)