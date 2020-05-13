def createTargetArray(nums, index):
    target = []
    for i in range(len(nums)):
        j = index[i]
        val = nums[i]
        target.insert(j, val)
    return target

# Without built in insert method

def createTargetArray2(nums, index):
    target = []
    for i in range(len(nums)):
        if index[i] == len(target):
            target.append(nums[i])
        else:
            target = target[:index[i]] + [nums[i]] + target[index[i]:]
    return target