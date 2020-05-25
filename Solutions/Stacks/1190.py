def solution(s):
    result = [""]
    for i in s:
        if i == "(":
            result.append("")
        elif i == ")":
            result[len(result)-2] += result.pop()[::-1]  # append the reversed last string to the second last string
        else:
            result[-1] += i
    return "".join(result)

