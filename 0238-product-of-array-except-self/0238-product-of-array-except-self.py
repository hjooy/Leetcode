class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix_product, suffix_product = 1, 1

        for i in range(len(nums)):
            ans[i] *= prefix_product
            prefix_product *= nums[i]
            ans[-1 - i] *= suffix_product
            suffix_product *= nums[-1 - i]

        return ans