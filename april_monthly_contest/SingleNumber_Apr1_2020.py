from collections import defaultdict
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


# My solution. A list approach:

# Time Complexity O(n**2) We iterate through the list, taking O(n) time. 
#   We search the whole list to find whether there is duplicate number, taking O(n) time. Because search is in the for loop, so we have to multiply both time complexities which results in O(n2).


# Space Complexity O(n)
    # We need a list of size n to contain elements in nums

def singleNumber(nums):
    no_2_nums = []
    for i in nums:
        if i not in no_2_nums:
            no_2_nums.append(i)
        else:
            no_2_nums.remove(i)
    return no_2_nums[0]

# Solution 2

# Using a hash table
# Time: O(n). Time complexity for for loop is O(n). Time complexity of hash table is O(1). And O(n*1) = O(n)
# Space: O(n). Space required by hash_table is equal to num of events in num.

def singleNumber2(nums):
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1
    
    for i in hash_table:
        if hash_table[i] == 1:
            return i


# Solution 3

# Using math
# Concept: 2∗(a+b+c)−(a+a+b+b+c)=c

# Time: O(n+n) = O(n). Sum calls next to iterate through the list. It can viewed as sum(list(i, for i in nums)) which is O(n) complexity because of number of elements in the list
# Space: O(n+n) = O(n). set uses space for the elements in nums

def singleNumber3(nums):
    return 2*sum(set(nums)) - sum(nums)

# Solution 4 (Most efficient!!)

# Bit manipulation
# Concept: 
    # If we take XOR of zero and some bit, it will return that bit:
        # a XOR 0 = a
    # If we take XOR of two same bits, it will return 0 
        # a XOR a = 0
    # So:
        # a XOR b XOR a = (a XOR a) XOR b = b (this is done in iteration for all the elements in the list)

# Time: O(n). We only iterate through the nums, so time complexity is the number of elements in nums
# Space: O(1)

def singleNumber4(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

