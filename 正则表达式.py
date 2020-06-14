def is_match_v1(text, pattern):
    """
    两个普通的字符串进⾏⽐较
    :param text:
    :param pattern:
    :return:
    """
    if len(text) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] != text[i]:
            return False
    return True


def is_match_v2(text, pattern):
    """
    v1 的递归版本
    :param text:
    :param pattern:
    :return:
    """
    i = 0
    j = 0
    while j < len(pattern):
        if i > len(text):
            return False
        if pattern[j] != text[i]:
            return False
        i += 1
        j += 1
    return j == len(text)


def is_match_v3(text, pattern) -> bool:
    """
    处理  .
    :param text:
    :param pattern:
    :return:
    """
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and is_match_v3(text[1:], pattern[1:])

def isMatch(text, pattern) -> bool:
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        # 发现 '*' 通配符
        pass
    else:
        return first_match and isMatch(text[1:], pattern[1:])