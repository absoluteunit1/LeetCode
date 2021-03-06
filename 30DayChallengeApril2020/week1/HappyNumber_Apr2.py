# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
# which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Ex:
# Input: 19
# Output: true
# Explanation: 
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1


# My solution

# I realized the hint was in the "...or it loops endlessly in a cycle" statement
# Since it loops endlessly in a CYCLE (meaning that the same numbers will start repeating in the loop), we need to keep track of that cycle. 
# The most efficient way to do so is using a hash table to store all the numbers of that "cycle"
# At each iteration, we check if the cycle is being repeated, if so, we return False since we will never reach 1. Otherwise, we keep iteration until we reach 1. 

def isHappy(num):
    n = str(num)
    nums = dict()
    while(num != 1):
        num = 0
        for i in n:
            num += int(i)**2
        n = str(num)
        if n in nums:
            return False
        nums[n] = num
    return True

# Fastest Solution

def isHappy(n):
    seen = set()
    result = 0  
    while result != 1:
        result = 0  
        while n > 0: 
            result += (n % 10) * (n % 10)    # Don't fully understand how this part works!?
            n = n // 10            
        if result == 1: 
            return True			
        elif result in seen: 
            return False
        else: 
            n = result      
            seen.add(n)  
    

