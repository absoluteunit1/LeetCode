# Brute force solution

def twoSum(nums, target):
    indices = []
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                indices.append(i)
                indices.append(j)
                return indices


def twoSum2(nums, target):
    indices = []
    