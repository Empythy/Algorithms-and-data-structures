def mountain_peak(arr):
    ret = 0
    for i in range(len(nums)):
        cur_item = nums[i]
        if i == 0:
            pre_item = float('-inf')
        else:
            pre_item = nums[i-1]
        if i == len(nums)-1:
            next_item = float('-inf')
        else:
            next_item = nums[i+1]
        if cur_item > pre_item and cur_item > next_item:
            ret = max(ret, i)
    print(ret)
if __name__ == "__main__":
    input_data = input()
    nums = [int(item) for item in input_data.split(" ")]

    mountain_peak(nums)