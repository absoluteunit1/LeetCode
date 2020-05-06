# My first solution
import collections
def canConstruct(ransomNote, magazine):
    letters = {i:magazine.count(i) for i in magazine}
    for i in ransomNote:
        if i in letters:
            if letters[i] > 0:
                letters[i] -= 1
            else:
                return False
        else:
            return False
    return True

# Another solution

def canConstruct2(ransomNote, magazine):
    

