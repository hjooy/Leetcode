class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0], nums[1])

        ans = 0

        # 1. nums[1:]
        dp1 = nums[1]
        dp2 = max(nums[1], nums[2])

        for n in nums[3:]:
            tmp = dp2
            dp2 = max(dp1 + n, dp2)
            dp1 = tmp
        
        ans = max(dp1, dp2)

        # 2. nums[:-1]
        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])
        
        for n in nums[2:-1]:
            tmp = dp2
            dp2 = max(dp1 + n, dp2)
            dp1 = tmp

        return max(ans, dp1, dp2)        