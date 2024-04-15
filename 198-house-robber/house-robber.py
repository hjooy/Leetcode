class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1, dp2 = 0, 0

        for n in nums:
            tmp = dp2
            dp2 = max(dp1 + n, dp2)
            dp1 = tmp

        return dp2