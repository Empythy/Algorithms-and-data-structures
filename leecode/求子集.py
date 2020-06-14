

def subset():
    ret = []
    nums = [1, 2, 3]
    allSet = 1 << len(nums)
    for i in range(allSet):
        item = []
        for j in range(len(nums)):
            if (i & (1 << j)):
                item.append(nums[j])
        ret.append(item)
    return ret




if __name__ == '__main__':
    ret = subset()
    print(ret)
    s = Solution()
    ret1 = s.subsetRecusive([1,2, 3])
    print(s.result)


