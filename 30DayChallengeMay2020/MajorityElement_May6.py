def majorityElement(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return max(d, key=d.get)

# Using colletions

import collections
def majorityElement2(nums):
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)
