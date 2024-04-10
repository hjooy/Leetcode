class Solution:
    def rob(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        if n == 1: return nums[0]
        elif n == 2: return max(nums[0], nums[1])
        
        dp1, dp2, dp3 = [0] * n, [0] * n, [0] * n
        
        # 1. sum includes nums[0] (excludes nums[1], nums[n - 1])
        dp1[0] = nums[0]
        for i in range(2, n - 1):
            if i < 4:
                dp1[i] = nums[i] + dp1[0]
            else:
                dp1[i] = nums[i] + max(dp1[i - 2], dp1[i - 3])

        # 2. sum includes nums[n - 1] (excludes nums[0], nums[n - 2])
        dp2[1] = nums[1]
        dp2[2] = nums[2]
        for i in range(3, n):
            dp2[i] = nums[i] + max(dp2[i - 2], dp2[i - 3])
        
        # 3. sum excludes both nums[0] and nums[n - 1]
        dp3[1] = nums[1]
        dp3[2] = nums[2]
        for i in range(3, n - 1):
            dp3[i] = nums[i] + max(dp3[i - 2], dp3[i - 3])
        
        for i in range(n):
            m = max(dp1[i], dp2[i], dp3[i])
            if ans < m: ans = m

        return ans