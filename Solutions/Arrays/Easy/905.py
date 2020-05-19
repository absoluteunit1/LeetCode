def sortByParrity(arr):
    even = []
    odd = []
    for i in arr:
        if i%2 == 1:
            odd.append(i)
        else:
            even.append(i)
    return even + odd

# Swaps in place

def sortByParrity2(A):
    i, j = 0, len(A) - 1
        # [3, 1, 2, 4]
        # i = 0, j = 3
    while i <= j:
        if A[i] % 2 != 1:
            i += 1
            continue
            
        if A[j] % 2 != 0:
            j -= 1
            continue
        
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
        
    return A