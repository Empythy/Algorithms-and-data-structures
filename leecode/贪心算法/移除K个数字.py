class Solution():

    def removeKdigits(self, num, k):
        stack = []
        for i in range(len(num)):
            number = int(num[i])
            while(len(stack)!=0 and stack[-1] > number):
                stack.pop()
                k -= 1
            if(number!=0 or len(stack)>0):
                stack.append(number)

        while(len(stack)!=0 and k>0):
            stack.pop()
            k -= 1

        result = []
        for i in range(len(stack)):
            result.append(str(stack[i]))
        if len(result) == 0:
            return "0"
        return "".join(result)

if __name__ == '__main__':
    num = "100001"
    k = 1
    s = Solution()
    ret = s.removeKdigits(num, k)
    print(ret)




