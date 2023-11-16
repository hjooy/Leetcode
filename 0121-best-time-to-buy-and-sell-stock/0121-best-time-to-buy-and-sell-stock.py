class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = 10000, 0
        
        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        
        return max_profit