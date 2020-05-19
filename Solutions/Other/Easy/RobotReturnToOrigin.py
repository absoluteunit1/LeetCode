def JudgeCircle(moves):
    origin = [0,0]
    for move in moves:
        if move == "U":
            origin[0] += 1
        elif move == "D":
            origin[0] -= 1
        elif move == "L":
            origin[1] -= 1
        elif move == "R":
            origin[1] += 1
    return origin == [0,0]

