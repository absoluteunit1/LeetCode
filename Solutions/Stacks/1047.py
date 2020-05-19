def solution(S):
    stack = []
    for i in S:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)
