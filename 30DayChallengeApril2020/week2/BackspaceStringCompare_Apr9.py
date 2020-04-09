
# My solution
# I used recursion to remove 2 elements (a letter and the following #) at each recursive iteration 


def backspace(strs):
    strs = strs.lstrip("#")
    n_b = strs.find("#")
    if n_b == -1:
        return strs
    return backspace(strs[:n_b-1] + strs[n_b+1:])

def backspaceCompare(S, T):
    return backspace(S) == backspace(T)
