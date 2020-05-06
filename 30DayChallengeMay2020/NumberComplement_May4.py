def findComplement(num):
    result = "0b"
    b = bin(num)
    for i in range(2, len(b)):
        if b[i] == "1":
            result += "0"
        else:
            result += "1"
    return int(result, 2)