
# My solution
# I used recursion to remove 2 elements (one letter and its following #) at each recursive call

def backspaceCompare(S, T):

    def backspace(strs):
        strs = strs.lstrip("#")
        n_b = strs.find("#")
        if n_b == -1:
            return strs
        return backspace(strs[:n_b-1] + strs[n_b+1:])

    return backspace(S) == backspace(T)

# Another solution. 
# Genius solution. Iterates through the string, and adds letters to a list. 
# When the char is the # symbol, it rmeoves the last entry from the list.
# Time: O(M + N), m and n are the lengths of s and t
# Space: O(M+N)
def backspaceCompare2(S, T):

    def finalString(s):
        stack = []
        for char in s:
            if stack and char == "#":
                stack.pop()
            elif char != "#":
                stack.append(char)
        return stack
    
    return finalString(S) == finalString(T)
