class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_set = Counter(s1)
        n1 = len(s1)
        n2 = len(s2)
        left = 0
        while left + n1 <= n2:
            if Counter(s2[left:left + n1]) == s1_set:
                print(s2[left:left + n1])
                return True
            else:
                left += 1
        return False

# s1 = "hello"
# s2 = "ooolleoooleh"
s1 = "ab"
s2 = "eidbaooo"
s = Solution()
res = s.checkInclusion(s1, s2)
print(res)