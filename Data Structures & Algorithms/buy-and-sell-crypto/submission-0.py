class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                if sell>0 and sell>buy:
                    max_profit = max(max_profit, sell-buy)
        return max_profit


        