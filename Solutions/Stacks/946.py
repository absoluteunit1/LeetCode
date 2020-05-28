def solution(pushed, popped):
    s = []
    for i in pushed:
        s.append(i)
        while popped and s:
            if popped[0] == s[-1]:
                s.pop()
                popped = popped[1:]
            else:
                break
    return False if s or popped else True


def solution2(pushed, popped):
    