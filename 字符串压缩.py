class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        ret = []
        cnt = 1
        char = S[0]
        for i in range(1, n):
            if char == S[i]:
                cnt += 1
            else:
                ret.extend([char, str(cnt)])
                char = S[i]
                cnt = 1
        ret.extend([char, str(cnt)])
        zip_s = "".join(ret)
        if len(zip_s)<len(S):
            return zip_s
        else:
            return S


