# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Solution 1 (43ms, beats 79.98%)
def maxProfit(prices: list[int]) -> int:
    min_price = max(prices)
    max_price = 0 
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if prices[i] - min_price > max_price:
            max_price = prices[i] - min_price
    return max_price

# solution youtube 
def maxProfit2(prices):
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit2(prices))