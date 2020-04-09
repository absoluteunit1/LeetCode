
# My initial solution: Brute force. Iterates through each subarray and replaces the max sum with sum of subarray if it is larger than current max sum value
# Passed 200/202 test cases but timed out on the other 2
# Has a time complexity of O(n**2) so it is not the most efficient approach. 

def maxSubArray(nums):
    l_sum = nums[0]
    l = len(nums)
    for i in range(l):
        for j in range(i, l):
            if sum(nums[i:j+1]) > l_sum:
                l_sum = sum(nums[i:j+1])
    return l_sum


# My second solution 
# Time complexity of O(n)
# At each iteration, we take the maximum value of either the current value or the current value + the previous max sum. 
# Good explanation at: https://youtu.be/58yMrWfUS7k?t=188

def maxSubArray3(nums):
    current_sum = nums[0]                                       # set the initial cur sum to the first value in the array
    maximum_sum = nums[0]                                       # set the initial max sum to the first value in the array
    for number in nums[1:]:                                     # iterate though the array, starting from the second value
        current_sum = max(current_sum + number, number)         # new current sum value: we choose the maximum of either the (previous current sum value + current value we are on in the array) or (the current value in the array)
        maximum_sum = max(maximum_sum, current_sum)             # the new maximum sum variable either remains unchanged (remains referencing the current value that maximum_sum holds) or we assign it the current_sums value. The max of either two
    return maximum_sum                                          # returns the max subarray value

