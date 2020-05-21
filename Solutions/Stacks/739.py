# Brute force solution (exceeds time limit)

def solution(T):
    r = []
    for i in range(len(T)):
        for j in range(i, len(T)):
            if T[j] > T[i]:
                r.append(j-i)
                found = True
                break
            else:
                found = False
        if found == False: r.append(0)
    return r

# Using stack and hashmap

def solution2(T):
    stack = []
    d = {}
    for i in range(len(T)):
        while stack and stack[-1][0] < T[i]:        # in the stack, store each entry as a tuple with the index and temp of each element 
            t = stack[-1]
            d[t[1]] = i - t[1]                      # whenever a larger temp is encountered, add the index diff between those two elements to the dict for its index, pop the previous and add the current to the stack
            stack.pop()
        stack.append((T[i], i))

    for i in range(len(T)):                         # replace the original values of T with the index differences or 0 if not in dict
        T[i] = d.get(i, 0)
    return T


# Shorted version of the solution above

def solution3(T):
    stack = []
    ans = [0 for _ in T]
    for i, v in enumerate(T):
        while stack and T[stack[-1]] < v:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans


