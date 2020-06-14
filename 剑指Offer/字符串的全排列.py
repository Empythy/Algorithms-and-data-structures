class Solution(object):

    def Perpution(self, ss):
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]

        charList = sorted(list(ss))
        ret = []
        for i in range(len(charList)):
            if i > 0 and [i] == ss[i - 1]:
                continue
            tmp = self.Perpution("".join(charList[:i]) + "".join(charList[i + 1:]))
            for item in tmp:
                ret.append(charList[i] + item)
        return ret


if __name__ == '__main__':
    ss = ""
    s = Solution()
    ret = s.Perpution(ss)
    print(ret)
