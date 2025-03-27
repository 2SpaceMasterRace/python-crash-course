def maxProfit(prices: List[int]) -> int:
#INPUT: array of prices where price[i] is the price of stock the current day
#OUTPUT: maximum profit 

    #Two-pointer method
    left,right = 0,1
    max_profit = 0

    while right != len(prices):
        if prices[left] < prices[right]:
            profit = prices[left] - prices[right]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1

    return max_profit
