def solution(target, n):
    operations = []
    for i in range(1, target[-1]+1):
        if i in target:
            operations.append("Push")
        else:
            operations.append("Push")
            operations.append("Pop")
    return operations


def solution2(target, n):
    i = 0
    r = []
    x = 1
    while i < len(target):
        r.append("Push")
        if x == target[i]:
            i += 1
        else:
            r.append("Pop")
        x += 1
    return r
    