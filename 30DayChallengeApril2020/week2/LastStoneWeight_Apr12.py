
# Recursive solution
# Approach
 
# Two Bases Cases: 
#   - no elements left, return 0
#   - one element left, return that element
# Recursive Call: 
#   - sort the array in an descending order 
#   - if the difference between the top two elements is zero, remove both and call the function on the array excluding the first two elements
#   - if the difference is not zero, call the function on the array excluding the first two elements and add a new element which is the difference between the two largest elements

def lastStoneWeight(stones):
    if stones == []:
        return 0
    elif len(stones) == 1:
        return stones[0]
    else:
        stones = sorted(stones, reverse=True)
        if stones[0] - stones[1] == 0:
            return lastStoneWeight(stones[2:])
        return lastStoneWeight(stones[2:] + [stones[0] - stones[1]])
    
# Iterative solution
# Approach

# Loop until there is 1 or 0 elements in the stones array
# Create a new array which is a slice of the stones array but excludes the two largest elements 
# Compare the two largest elements, if they are not the same, append to the new array
# Set the sorted new array to the stones array variable and repeat the loop. 

def lastStoneWeight2(stones):
    stones.sort(reverse=True)
    while len(stones) > 1:
        arr = stones[2:]
        y = stones[0]
        x = stones[1]
        if x != y:
            arr.append(y-x)
        stones = sorted(arr, reverse=True)
    if stones:
        return stones[0]
    return 0