def replaceElements(arr):
    arr = arr[len(arr)-1::-1]
    result = [-1]
    for i in range(len(arr) - 1):
        result = [max(arr[:i+1])] + result
    return result

# Faster solution

def replaceElements2(arr):
    mx = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], mx = mx, max(arr[i], mx)
    return arr
    