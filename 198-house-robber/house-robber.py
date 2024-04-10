class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i, n in enumerate(nums):
            if i <= 1: dp[i] = n
            elif i < 3:
                dp[i] = n + dp[i - 2]
            else:
                dp[i] = n + max(dp[i - 2], dp[i - 3])
        
        return max(dp)