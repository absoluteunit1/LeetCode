def solution(startTime, endTime, queryTime):
    num = 0
    for i in range(len(startTime)):
        if queryTime >= startTime[i] and queryTime <= endTime[i]:
            num += 1
    return num
