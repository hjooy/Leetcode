class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [ 0 for _ in range(len(nums)) ]
        forward = []
        backward = []
        accumulated_product = 1
        for num in nums:
            accumulated_product *= num
            forward.append(accumulated_product)
        
        accumulated_product = 1
        for i in range(len(nums) - 1, -1, -1):
            accumulated_product *= nums[i]
            backward.insert(0, accumulated_product)
        
        for i in range(len(nums)):
            if i - 1 < 0:
                ans[i] = backward[i + 1]
            elif i + 1 >= len(nums):
                ans[i] = forward[i - 1]
            else:
                ans[i] = forward[i - 1] * backward[i + 1]
        
        return ans