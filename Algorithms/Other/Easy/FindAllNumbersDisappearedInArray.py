# Solution using sets
# Approach

# Turn the given array into a set
# Generate a set of numbers from 1, to the length of the given array 
# Perform the difference operation; we will get a list of numbers that are not in A. 

def findDisappearedNumbers(nums):
    if nums:
        a = set(nums)
        b = set([i for i in range(1, len(nums) + 1)])
        return list(b.difference(a))
    return []

