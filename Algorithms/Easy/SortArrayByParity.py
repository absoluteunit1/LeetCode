# My solution

def sortArray(A):
    odd = [i for i in A if i%2 == 1]
    even = [i for i in A if i%2 == 0]
    final = []
    for i in range(len(A)):
        if i%2 == 1:
            final.append(odd[0])
            odd.pop(0)
        elif i%2 == 0:
            final.append(even[0])
            even.pop(0)
    return final

# Other Solutions

# Time Complexity O(N)
# Space Complexity O(N)

def sortArray2(A):
    final = [None]*len(A)
    t = 0
    for i, v in enumerate(A):
        if v%2 == 0:
            final[t] = v
            t += 2
    t = 1
    for i, v in enumerate(A):
        if v%2 == 1:
            final[t] = v
            t += 2
    return final

