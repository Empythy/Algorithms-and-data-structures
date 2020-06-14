from functools import lru_cache


def isMatch_v1(text, pattern) -> bool:
    """
    判断两个字符串值是否相等
    :param text:
    :param pattern:
    :return:
    """
    if len(pattern) ==0:
        return len(text) ==0

    first_match = False
    if bool(text) and pattern[0] == text[0]:
        first_match = True
    return first_match and isMatch_v1(text[1:], pattern[1:])


def isMatch_v2(text, pattern) -> bool:
    """
    判断两个字符串值是否相等  含有.
    :param text:
    :param pattern:
    :return:
    """
    if len(pattern) == 0:
        return len(text) == 0

    first_match = False
    if bool(text) and pattern[0] in [text[0] ,'.'] :
        first_match = True
    return first_match and isMatch_v2(text[1:], pattern[1:])


@lru_cache(None)
def isMatch_v3(text, pattern) -> bool:
    """
    判断两个字符串值是否相等  含有.
    :param text:
    :param pattern:
    :return:
    """
    # if len(pattern) == 0:
    #     return len(text) == 0
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    # first_match = False
    # if bool(text) and pattern[0] in [text[0] ,'.'] :
    #     first_match = True
    if len(pattern)>=2 and pattern[1] == "*":
        # 发现通配符
        return isMatch_v3(text, pattern[2:]) or \
            first_match and isMatch_v3(text[1:], pattern)

    return first_match and isMatch_v3(text[1:], pattern[1:])



class Solution:
    from functools import lru_cache
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        """
       判断两个字符串值是否相等  含有.
        :param text:
        :param pattern:
        :return:
        """
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p)>=2 and p[1] == "*":
            #              匹配0次                          匹配1次
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        return first_match and self.isMatch(s[1:], p[1:])

if __name__ == "__main__":
    s = "aa"
    p = "a*"
    solution = Solution()
    res = solution.isMatch(s, p)
    print(res)