def solution(arr):
    count, max_count = 0, 0, 0
    for i in arr:
        if i == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max(max_count, count) 


