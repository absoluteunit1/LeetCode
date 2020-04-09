# My first solution. Passes 20/21 test cases. Exceeds time limit on the last case

def moveZeroes2(nums):
    i = 1
    while(True):
        if len(nums) == 1:
            break
        elif nums[i] != 0 and nums[i-1] == 0:
            nums[i-1] = nums[i]
            nums[i] = 0
            i = 1
        elif i == len(nums) - 1:
            break
        else:
            i += 1

# Fastest solution. O(n) time. 
def moveZeroes3(nums):
    index = 0                           
    for i in range(len(nums)):          
        if nums[i] != 0:                
            nums[index] = nums[i]       
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0 
    



    





