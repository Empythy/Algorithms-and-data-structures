
import bisect
line1 = "2"
line2 = "2 1 4 3"
line3 = "4"
line4 = "1 2 0 2"

n = int(line1)
nums = list(map(int, line2.split()))
m = int(line3)
q = list(map(int, line4.split()))

def reverse_count(nums):
    ans = 0
    sorted_num = [nums[-1]]
    for i in range(len(nums)-2, -1, -1):
        left = bisect.bisect_left(sorted_num, nums[i])
        # print(f"{sorted_num} \t {nums[i]} \t {left}")
        ans += left
        bisect.insort_left(sorted_num, nums[i])
    # print(sorted_num)
    return ans

def group_and_reverse(nums, group_len):
    if len(nums) == 0:
        return []
    group_len = min(group_len, len(nums))
    return nums[:group_len][::-1] + group_and_reverse(nums[group_len:], group_len)
for i in range(m):
    q_i = q[i]
    # print(f"q_i = {q_i}")
    nums = group_and_reverse(nums, 2**q_i)
    # print(f"new_nums={nums}")
    ans = reverse_count(nums)
    print(ans)

