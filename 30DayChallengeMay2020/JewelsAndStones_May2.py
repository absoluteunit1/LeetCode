def numJewelsIsInStones(J, S):
    c = 0
    for i in S:
        if i in J:
            c += 1
    return c