# First solution

def solution(s, k):
    i, stack, p = 0, [], 0
    while i < len(s):
        if stack and stack[-1] == s[i]:
            stack.append(s[i])
            i += 1
            if len(stack) == k:
                s = s[:p] + s[p+k:]
                stack = []
                i = 0
        else:
            p = i
            stack = [s[i]]
            i += 1
    return s

# Solution from the discussion section

def solution3(s, k):
    stack = [['#', 0]]
    for c in s:
        if stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])
    return ''.join(c * k for c, k in stack)
