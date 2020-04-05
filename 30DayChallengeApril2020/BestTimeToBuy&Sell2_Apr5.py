
# My initial solution:
# Time O(n)

def maxProfit(prices):
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] - prices[i] > 0:
            profit += (prices[i+1] - prices[i])
    return profit



a = [7,1,5,3,6,4]
b = [1,2,3,4,5]
c = [7,6,4,3,1]
d = [2,4,1]

print(maxProfit(a))
print(maxProfit(b))
print(maxProfit(c))
print(maxProfit(d))

