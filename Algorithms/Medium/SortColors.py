def sortColors(nums):
    r, b, w = 0, 0, 0
    for i in nums:
        if i == 0:
            r += 1
        elif i == 1:
            w += 1
        else:
            b +=1

    for i in range(len(nums)):
        if r != 0:
            nums[i] = 0
            r -= 1
        elif b != 0:
            nums[i] = 1
            b -= 1
        elif w != 0:
            nums[i] = 2
            w -= 1
    return nums
