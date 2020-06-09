def solution(str1):
    result = ""
    for char in str1:
        if ord(char) < 91 and ord(char) > 64:
            result += chr(ord(char) + 32)
        else:
            result += char
    return result
