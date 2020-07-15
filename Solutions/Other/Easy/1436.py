def solution(paths):
    cur = paths[0][1]
    outGoing = True
    while outGoing:
        for i in paths:
            if i[0] == cur:
                cur = i[1]
                break
            

