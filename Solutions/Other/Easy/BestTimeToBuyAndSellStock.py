# Brute Force Solution
# Times out on one case: 199/200 passed

def maxProfit(prices):
    highestProfit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > highestProfit:
                highestProfit = prices[j] - prices[i]
    return highestProfit


# More intelligent solution 
# Uses maxSubarraySum logic

def maxProfit2(prices):
    higher_profit = 0
    if len(prices) > 1:
        changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        higher_num = changes[0]
        for i in range(1, len(changes)):
            higher_num = max(changes[i], changes[i] + higher_num)
            if higher_num > highest_profit:
                highest_profit = higher_num
    return highest_profit


print(maxProfit2([7,1,5,3,6,4]))

