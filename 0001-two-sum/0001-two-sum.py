class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):          # O(n)
            if target - nums[i] in dict:    # O(1) 
                return [i, dict[target - nums[i]]]
            dict[nums[i]] = i
        return []

# Time complexity: O(n)
# Space complexity: O(n)