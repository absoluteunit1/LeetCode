# Brute force
def solution(words, chars):
    result = 0
    g = dict()
    for char in chars:
        g[char] = chars.count(char)
    for word in words:
        temp = 0
        for letter in word:
            if letter not in g or g[letter]<word.count(letter):
                temp = 1
                break
        if temp == 0:
            result += len(word)
    return result






