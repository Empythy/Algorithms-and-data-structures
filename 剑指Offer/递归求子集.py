class Solution(object):
    def __init__(self):
        self.item = []
        self.result = []

    def subsetRecusive(self, nums):
        self.generate(nums, index=0)

    def generate(self, nums, index):
        if index >= len(nums):
            return
        self.item.append(nums[index])
        self.result.append(self.item[:])
        index += 1
        self.generate(nums, index)
        self.item.pop()
        self.generate(nums, index)

if __name__ == '__main__':
    s = Solution()
    s.subsetRecusive([1,2,3])
    print(s.result)
