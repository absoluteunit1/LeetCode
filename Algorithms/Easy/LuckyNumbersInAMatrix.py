def luckyNumbers(matrix):
    min1 = []
    max1 = matrix[0]
    
    for i in range(len(matrix)):
        min1.append(min(matrix[i]))
        max1 = list(map(lambda x, y: max(x, y), matrix[i], max1))
    return list(set(min1) & set(max1))

