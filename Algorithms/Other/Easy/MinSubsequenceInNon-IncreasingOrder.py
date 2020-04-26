def minSequence(nums):
    nums = sorted(nums, reverse=True)
    i = 0
    if len(nums) == 1 or len(nums) == 0:
        return nums
    else:
        while(sum(nums[:i]) <= sum(nums[i:])):
            i += 1
    return nums[:i]

