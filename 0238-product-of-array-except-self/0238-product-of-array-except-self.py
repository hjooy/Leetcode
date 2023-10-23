class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [ 1 for _ in range(len(nums)) ]
        
        accumulated_product = 1
        for i in range(len(nums) - 1):
            accumulated_product *= nums[i]
            ans[i + 1] = ans[i + 1] * accumulated_product
        
        accumulated_product = 1
        for i in range(len(nums) - 1, 0, -1):
            accumulated_product *= nums[i]
            ans[i - 1] = ans[i - 1] * accumulated_product

        return ans