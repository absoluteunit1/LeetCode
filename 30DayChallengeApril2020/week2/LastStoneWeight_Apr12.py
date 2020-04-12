
# Recursive solution

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