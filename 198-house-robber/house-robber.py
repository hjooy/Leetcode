class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        dp1 = nums[0]
        dp2 = max(nums[1], nums[0])

        for n in nums[2:]:
            tmp = dp2
            dp2 = max(dp1 + n, dp2)
            dp1 = tmp

        return max(dp1, dp2)