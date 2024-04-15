class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        dp1 = nums[0]
        dp2 = nums[1] if nums[1] > nums[0] else nums[0]

        for n in nums[2:]:
            tmp = dp2
            dp2 = dp1 + n if dp1 + n > dp2 else dp2
            dp1 = tmp

        return dp1 if dp1 > dp2 else dp2