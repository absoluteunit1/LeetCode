def smallerNums(nums):
    nums2 = []
    c = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                c += 1
        nums2.append(c)
        c = 0
    return nums2

