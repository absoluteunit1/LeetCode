# Brute force solution

def solution(nums1, nums2):
    result = []
    for i in nums1:
        j = nums2.index(i)
        for k in nums2[j::]:
            if k > i:
                result.append(k)
                noGreater = False
                break
            else:
                noGreater = True
        if noGreater:
            result.append(-1)
    return result


# Using a stack and a hash map

def solution2(nums1, nums2):
    d = {}
    s = []
    # Very usefull snippet for finding the next greatest element in an array
    for i in nums2:
        while s and s[-1] < i:      
            d[s.pop()] = i
        s.append(i)
    
    for i in range(len(nums1)):
        nums1[i] = d.get(nums1[i], -1)
    return nums1