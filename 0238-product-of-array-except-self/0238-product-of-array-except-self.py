class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [ 1 for _ in range(len(nums)) ]
        
        forward_product = 1
        backward_product = 1
        for i in range(len(nums) - 1):
            forward_product *= nums[i]
            backward_product *= nums[len(nums) - 1 - i]
            ans[i + 1] = ans[i + 1] * forward_product
            ans[len(nums) - 2 - i] = ans[len(nums) - 2 - i] * backward_product

        return ans