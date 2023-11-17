class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = len(prices) - 1
        max_profit, highest = 0, right
        
        while right >= 0:
            if prices[right] > prices[highest]:
                highest = right
            else:
                max_profit = max(max_profit, prices[highest] - prices[right])
            right -= 1
        
        return max_profit