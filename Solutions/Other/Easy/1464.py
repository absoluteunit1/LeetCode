# Brute force. Iterate over the array; using a variable to keep track of the maximum value
def solution(nums):
    maximum = 0
    for i in range(len(nums) - 1) :
        for j in range(1, len(nums)):
            if (nums[i]-1)*(nums[j]-1) > maximum and i != j:
                maximum = (nums[i]-1)*(nums[j]-1)
    return maximum

# Sort, use last two values
def solution(nums):
    nums = sorted(nums)
    return (nums[-1]-1)*(nums[-2]-1)

# One pass. O(n) runtime
def solution(nums):
    n = m = 0
    for num in nums:
        if num >= m:
            n = m
            m = num
        elif num > n:
            n = num
    return (m - 1)*(n - 1)
    