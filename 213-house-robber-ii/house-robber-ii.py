class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        dp1, dp2, ans = 0, 0, 0

        # 1. nums[1:]
        for n in nums[1:]:
            tmp = dp2
            dp2 = max(dp1 + n, dp2)
            dp1 = tmp
        
        ans = dp2

        # 2. nums[:-1]
        dp1, dp2 = 0, 0
        
        for n in nums[:-1]:
            tmp = dp2
            dp2 = max(dp1 + n, dp2)
            dp1 = tmp

        return max(ans, dp2)        