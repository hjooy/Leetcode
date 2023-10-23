class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [ 1 for _ in range(n) ]
        
        forward_product = 1
        backward_product = 1
        for i in range(n - 1):
            forward_product *= nums[i]
            backward_product *= nums[n - 1 - i]
            ans[i + 1] = ans[i + 1] * forward_product
            ans[n - 2 - i] = ans[n - 2 - i] * backward_product

        return ans