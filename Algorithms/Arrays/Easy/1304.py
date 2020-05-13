def sumZero(n):
    if n%2 == 1:
        return [i for i in range(-n//2 + 1, n//2 + 1)]
    return [i for i in range(-n/2, n/2 + 1) if i != 0]