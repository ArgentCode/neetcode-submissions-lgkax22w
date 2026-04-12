class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            buy = prices[i]
            for j in range(i+1, n):
                sell = prices[j]
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit
        return(max_profit)