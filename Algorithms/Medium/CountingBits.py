# My solution 

def countBits(num):
    return [str(bin(i)).count("1") for i in range(num + 1)]

