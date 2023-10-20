class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        dict = {}
        for i in range(len(nums)):          # O(n)
            complement = target - nums[i]
            if complement in dict:          # O(1) 
                ans = [i, dict.get(complement)]
                break
            else: dict[nums[i]] = i
        return ans

# Time complexity: O(n)
# Space complexity: O(n)