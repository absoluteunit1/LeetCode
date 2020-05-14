def solution(A):
    result = []
    d = dict()
    word = A[0]
    for letter in word:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    
    
    if len(A) > 1:
        A = A[1:]
        for word in A:
            for i in d:
                if i in word and d[i] > word.count(i):
                    d[i] -= (d[i] -word.count(i))
                elif i not in word:
                    d[i] = -1

    for i in d:
        if d[i] != -1:
            result += [i]*d[i]
    return result