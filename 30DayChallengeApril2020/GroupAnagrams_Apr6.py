import collections

# MY SOLUTION

# I used a sorted word as a key in a dictionary, and if the key exists, I append the word to the list at that key
# if the key does not exist, I assign the word in in a list as a value for that key 

def groupAnagrams(strs):
    d = {}
    for word in strs:
        a = "".join(sorted(word))
        if a in d:
            d[a].append(word)
        else:
            d[a] = [word]
    return d.values()


# OTHER SOLUTIONS


# Using a sorted string but as a tuple as the key instead

def groupAnagrams2(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

# Categorizing by count

def groupAnagrams3(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()