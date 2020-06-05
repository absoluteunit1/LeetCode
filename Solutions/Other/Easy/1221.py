def solution(s):
    b, c = 0, 0
    for i in s:
        if i == "L": b -= 1
        elif i == "R": b += 1
        if b == 0: c += 1
    return c