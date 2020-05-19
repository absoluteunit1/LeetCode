def findNumbers(nums):
    evenDigits = 0
    for i in nums:
        if len(str(i))%2 == 0:
            evenDigits += 1
    return evenDigits

