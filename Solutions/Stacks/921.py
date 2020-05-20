def solution(S):
    lb, rb, l = 0, 0, "("
    for i in S:
        if i == l:
            lb += 1
        else:
            if lb: lb -= 1
            else: rb += 1
    return lb + rb

