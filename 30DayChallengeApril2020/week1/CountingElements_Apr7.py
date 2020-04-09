
# My solution
# Passed all test cases

def countElements(arr):
    a = set(arr)
    count = 0
    for i in arr:
        if i+1 in a:
            count += 1
    return count


