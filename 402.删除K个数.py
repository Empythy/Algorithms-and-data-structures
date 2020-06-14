class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        try:
            while num[0] == '0': num = num[1:]
        except:
            return '0'

        if len(num) == 1 and k == 1: return '0'
        if k == 0: return num

        for i in range(len(num) - 1):
            if num[i + 1] < num[i]:
                # 如果下一个数字 小于 当前数字 就移除当前数字
                return self.removeKdigits(num[:i] + num[i + 1:], k - 1)
            # 如果后一位数字比当前数字大  需要直接删除后面的数字
            if i == len(num) - 2:
                return self.removeKdigits(num[:-1], k - 1)


class Solution1:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for i in range(len(num)):
            while k and res and num[i] < res[-1]:
                # 当前位 小于 上一位  就抛出上一位数
                res.pop()
                k -= 1
            res += num[i]
        if k:
            res = res[:-k]

        if len(res) == 0: return '0'
        return str(int(''.join(res)))
        # i = 0
        # print("1", res)
        # while i < len(res) and res[i] == '0':
        #     i += 1
        #
        # if i == len(res):
        #     return '0'
        # else:
        #     return ''.join(res[i:])


if __name__ == "__main__":
    l = "112"
    k = 1
    s = Solution()
    res = s.removeKdigits(l, k)
    print(res)
