class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            dict[num] = i
        
        for i, num in enumerate(nums):
            if target - num in dict and i != dict[target - num]:
                return [i, dict[target - num]]

        return []

# Time complexity: O(n)
# Space complexity: O(n)