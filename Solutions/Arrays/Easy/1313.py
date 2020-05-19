def decompressRLElist(nums):
    l = len(nums)
    i = 0
    result = []
    while i < l:
        result += [nums[i+1]]*nums[i]
        i += 2
    return result
        
def decompressRLElist(nums):
    freq = nums[0::2]
    val = nums[1::2]
    result = []
    for i in range(len(freq)):
        result += [val[i]]*freq[i]
    return result