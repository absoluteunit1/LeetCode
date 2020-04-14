
# My solution 

def shiftStrings(s, shift):
    l = len(s)
    for order in shift:
        direction = order[0]
        amount = order[1]
        if direction == 1:
            s_r = amount%l
            if s_r != 0:
                s = s[l - s_r:l] + s[:l - s_r]
        else:
            s_l = amount%l
            if s_l != 0:
                s = s[s_l:l] + s[:s_l]
    return s
