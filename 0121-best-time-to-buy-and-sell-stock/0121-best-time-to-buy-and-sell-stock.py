class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, lowest = 0, 0
        
        for i in range(len(prices)):
            if prices[lowest] > prices[i]:
                lowest = i
            else:
                max_profit = max(max_profit, prices[i] - prices[lowest])
        
        return max_profit