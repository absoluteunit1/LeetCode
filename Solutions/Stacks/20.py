def solution(s):
    if s:
        lefty = "({["
        righty = ")}]"
        stack = []
        for c in s:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if not stack:
                    return False
                elif lefty.index(stack.pop()) != righty.index(c):
                    return False 
        if stack:
            return False
    return True
