def numberOfsteps(num):
    c = 0
    while num:
        if num%2 == 1:
            num -= 1
        else:
            num /= 2
        c += 1
    return c

    